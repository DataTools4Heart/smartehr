"""Graded and medication features from Dutch clinical narrative.

WHY THIS EXISTS. The T3-0 headroom check (docs/t3-frozen-llm-plan.md §3.3) showed that
chart-derivable curated variables reach test C 0.7310 against demographics' 0.6727, while
every text arm so far reached 0.6750. The gap is not "which facts are recorded" but the
FORM they are recorded in: every top carrier is graded or dated, and both TF-IDF and the
binary concept arm encode only presence.

  stenACIl  0.6471   percent carotid stenosis       vs  concept.stenose_present  0.4924
  packyrs   0.6182   pack-years                     vs  concept.roken_present    0.5021
  KliMaYr   0.3855   year of the first event        vs  (no dated feature exists)
  mht_alln  0.5732   COUNT of antihypertensive classes  vs  (removed as a medication tier)

So this module extracts quantities and dates, not assertions.

GROUNDING. Every scale here reproduces a definition in the project's own registry
dictionary, data/smartehr/data_dicts/smart.csv, so an extracted feature is on the same
scale as the curated variable it mirrors and the two are directly comparable:

  stenosis grade  stenACIl/stenACIr: 0 geen, 1 <=29%, 2 30-49%, 3 50-69%, 4 >=70%,
                  5 subtotaal, 6 occlusie, 7 pre-occlusief
  csten_50/70     "Niet/wel carotis stenose >= 50% / >= 70% (duplex)" -> thresholds on
                  that same grade
  pack-years      packyrs: "Aantal pakjes sig./shag (van 20) per dag keer aantal jaren
                  gerookt" -- a pack is 20, stated in the label itself
  smoking         roken: 0 nooit, 1 vroeger, 3 momenteel (NB there is no code 2)
  alcohol         alcohol: 0 nooit, 1 vroeger, 2 recent gestopt/nog steeds, 3 momenteel
  glasses/week    AlchlGlz: 0 geen, 1 <1, 2 1-10, 3 11-20, 4 21-30, 5 31-40, 6 >40
  onset year      KliMaYr: "Jaar eerste uiting klin.manifest vaatlijden" -- so the
                  EARLIEST year in a vascular context, not the latest
  aorta diameter  aorta_hg: "Grootste diameter aorta (cm.)" -- so the MAXIMUM, in cm

What is NOT grounded in the repo -- chiefly the mapping from SMART's internal L10/L20/D20
medication groups to ATC prefixes, and the Dutch surface forms that express each scale --
is recorded in ASSUMPTIONS.md rather than left implicit.

The medication lexicon is not hard-coded: ATC prefixes below define each class, and the
Dutch drug NAMES for them are derived from the cohort's own med_20250709.csv
(med_ZIatc + med_genNaam, documented in data_dict.csv as "Medication ATC code" /
"Medication name"), train patients only. Writing drug lists by hand would be exactly the
kind of ungrounded guess that the prefix-partition mistake already cost us once.
"""

import re
import unicodedata

# ---------------------------------------------------------------- shared text handling

def norm(text):
    """Lowercase, strip accents, collapse whitespace. Keeps %, digits, . and , intact."""
    if not text:
        return ""
    t = unicodedata.normalize("NFKD", str(text).lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", t)


def _num(s):
    """Dutch decimals use a comma. '5,5' -> 5.5"""
    try:
        return float(s.replace(",", "."))
    except (ValueError, AttributeError):
        return None


# Negation cues, reused from the concept extractor's NegEx-style rule. For a GRADED
# feature negation usually means the scale's zero rather than a missing value: the
# registry codes "geen stenose of plaque" as 0, not as absent.
NEG_CUES = ("geen", "niet", "zonder", "negatief", "uitgesloten", "nooit", "afwezig")


# ---------------------------------------------------------------- 1. carotid stenosis grade
#
# stenACIl / stenACIr, codes 0-7. A percentage in the text is mapped through the
# registry's own bands, so 65% becomes 3 exactly as the study visit would have coded it.

STENOSIS_TERMS = r"(?:stenose|stenosis|vernauwing|occlusie|afsluiting|plaque)"
VESSEL_TERMS = r"(?:aci|a\.?\s?carotis\s?interna|carotis|halsslagader|carotiden)"

# Dutch severity words, mapped to the band whose definition they name. "geringe" is
# explicitly the <=29% band, "matige" the 30-49% one and "ernstige" the >=70% one in
# routine Dutch duplex reporting; this word->band step is an ASSUMPTION (see
# ASSUMPTIONS.md #4), the percent->band step is not.
# `standalone` marks a term that names the lesion itself, so it needs no stenosis noun
# beside it: "occlusie van de ACI links" states a finding on its own, whereas "ernstige"
# is only a modifier and must qualify one ("ernstige stenose").
QUALITATIVE = (
    (r"pre-?occlusief|pre-?occlusieve?", 7, True),
    (r"(?:totale?\s+)?occlusie|geoccludeerd|volledig afgesloten|afsluiting", 6, True),
    (r"subtotale?", 5, False),
    (r"ernstige?|forse?|hooggradige?|significante?", 4, False),
    (r"matige?|middelmatige?|matig-?ernstige?", 2, False),
    (r"geringe?|lichte?|minimale?|laaggradige?|niet-?significante?", 1, False),
)

WINDOW = 60          # characters between a vessel/stenosis term and its quantity
TIGHT_WINDOW = 30    # for a term that IS the lesion, so it must sit beside the vessel
LATERAL_WINDOW = 40  # characters within which "links"/"rechts" binds to the finding


def pct_to_grade(pct):
    """Map a stenosis percentage onto the stenACI* code. Registry bands, verbatim."""
    if pct is None or pct < 0 or pct > 100:
        return None
    if pct == 0:
        return 0
    if pct <= 29:
        return 1
    if pct <= 49:
        return 2
    if pct <= 69:
        return 3
    return 4


def _side(context):
    """Which carotid the finding refers to, from the words around it."""
    left = re.search(r"\b(links?|linker|l\.)\b", context)
    right = re.search(r"\b(rechts?|rechter|r\.)\b", context)
    if left and not right:
        return "left"
    if right and not left:
        return "right"
    return None       # bilateral, or unstated -> counted only in the side-agnostic feature


def extract_stenosis(text):
    """-> list of (grade, side) findings. Grades are on the stenACI* 0-7 scale."""
    t = norm(text)
    out = []
    # A percentage only counts when it sits next to a stenosis or carotid term, or
    # "70% van de patienten" and every other stray percentage would become a finding.
    for m in re.finditer(r"(\d{1,3})\s*(?:-\s*(\d{1,3})\s*)?%", t):
        lo, hi = int(m.group(1)), (int(m.group(2)) if m.group(2) else None)
        ctx = t[max(0, m.start() - WINDOW):m.end() + WINDOW]
        if not (re.search(STENOSIS_TERMS, ctx) and re.search(VESSEL_TERMS, ctx)):
            continue
        # A reported range is coded by its UPPER bound: "50-69%" is the registry's own
        # band 3, and taking the lower bound would systematically under-grade.
        g = pct_to_grade(hi if hi is not None else lo)
        if g is not None:
            out.append((g, _side(t[max(0, m.start() - LATERAL_WINDOW):
                                  m.end() + LATERAL_WINDOW])))
    # Qualitative gradings, and explicit absence -> the scale's 0.
    for m in re.finditer(VESSEL_TERMS, t):
        ctx_from = max(0, m.start() - WINDOW)
        ctx = t[ctx_from:m.end() + WINDOW]
        tight = t[max(0, m.start() - TIGHT_WINDOW):m.end() + TIGHT_WINDOW]
        if not re.search(STENOSIS_TERMS, ctx):
            continue
        if re.search(r"\b(?:geen|zonder|vrij van)\b[^.;]{0,30}" + STENOSIS_TERMS, ctx) or \
           re.search(STENOSIS_TERMS + r"[^.;]{0,20}\b(?:afwezig|niet aanwezig)\b", ctx):
            out.append((0, _side(t[ctx_from:m.end() + LATERAL_WINDOW])))
            continue
        if re.search(r"\d{1,3}\s*%", ctx):
            continue          # already captured, quantitatively
        for pat, grade, standalone in QUALITATIVE:
            hit = (re.search(r"\b(?:" + pat + r")\b[^.;]{0,25}" + STENOSIS_TERMS, ctx)
                   or re.search(STENOSIS_TERMS + r"[^.;]{0,25}\b(?:" + pat + r")\b", ctx)
                   # A standalone lesion term still has to sit NEXT TO the vessel, within
                   # TIGHT_WINDOW, or any occlusion mentioned elsewhere in the report is
                   # attributed to the carotid.
                   or (standalone and re.search(r"\b(?:" + pat + r")\b", tight)))
            if hit:
                out.append((grade, _side(t[ctx_from:m.end() + LATERAL_WINDOW])))
                break
    return out


# ---------------------------------------------------------------- 2. pack-years
#
# packyrs: "Aantal pakjes sig./shag (van 20) per dag keer aantal jaren gerookt".
# The label fixes a pack at 20, so cigarettes/day / 20 = packs/day.

CIGS_PER_PACK = 20


def extract_packyears(text, reconstruct=True):
    """-> list of pack-year values. Stated figures only, unless `reconstruct`.

    `py` was removed from the alternation: as an abbreviation it matches anything ("10 py")
    and the validated agreement with `packyrs` could not distinguish a bad abbreviation
    from a bad reconstruction. The builder now emits stated and reconstructed values as
    SEPARATE features for exactly that reason.
    """
    t = norm(text)
    out = []
    for m in re.finditer(r"(\d{1,3}(?:[.,]\d+)?)\s*(?:pack\s?-?\s?years?|packyears?|"
                         r"pakjaar|pakjaren)\b", t):
        v = _num(m.group(1))
        if v is not None and 0 <= v <= 200:
            out.append(v)
    if out or not reconstruct:
        return out          # a stated pack-year figure beats anything reconstructed
    # Reconstruct only when BOTH a rate and a duration are present; a rate alone gives
    # no pack-years, and defaulting the missing half would invent the quantity.
    rate = None
    m = re.search(r"(\d{1,3})\s*(?:sigaretten|sig\.?|shag)\s*(?:per|/)\s*dag", t)
    if m:
        rate = int(m.group(1)) / CIGS_PER_PACK
    if rate is None:
        m = re.search(r"(\d{1,2}(?:[.,]\d+)?)\s*(?:pakje|pakjes|pakje\(s\))\s*(?:per|/)\s*dag", t)
        if m:
            rate = _num(m.group(1))
    if rate is None:
        return out
    years = None
    m = re.search(r"(?:sinds|gedurende|al)\s*(\d{1,2})\s*jaar", t)
    if m:
        years = int(m.group(1))
    else:
        m = re.search(r"(\d{1,2})\s*jaar\s*(?:gerookt|roken)", t)
        if m:
            years = int(m.group(1))
    if years is not None:
        v = rate * years
        if 0 <= v <= 200:
            out.append(v)
    return out


# ---------------------------------------------------------------- 3. smoking status
#
# roken: 0 nooit gerookt, 1 vroeger gerookt, 3 rookt momenteel. There is no code 2, and
# the codes are kept as-is so the feature is on the curated variable's scale.

SMOKING_NEVER = r"\b(?:nooit gerookt|niet-?roker|non-?smoker|nooit geroken)\b"
SMOKING_FORMER = (r"\b(?:ex-?roker|ex-?rookster|voormalig(?:e)? roker|gestopt met roken|"
                  r"gestopt te roken|vroeger gerookt|rookte voorheen|"
                  r"rookt niet meer|niet meer gerookt)\b")
SMOKING_CURRENT = r"\b(?:rookt|roker|rookster|actief roker|nog steeds rookt|rookt nog)\b"


def extract_smoking_status(text):
    """-> 0 / 1 / 3 on the `roken` scale, or None.

    Order matters and is not arbitrary: 'ex-roker' contains 'roker' and 'gestopt met
    roken' contains 'roken', so the more specific never/former patterns must be tested
    before the current-smoker one or every ex-smoker reads as a current smoker.
    """
    t = norm(text)
    if re.search(SMOKING_NEVER, t):
        return 0
    if re.search(SMOKING_FORMER, t):
        return 1
    if re.search(SMOKING_CURRENT, t):
        return 3
    return None


# ---------------------------------------------------------------- 4. alcohol
#
# alcohol: 0 nooit, 1 vroeger, 2 recent gestopt/nog steeds, 3 momenteel.
# AlchlGlz bands: 0 geen, 1 <1, 2 1-10, 3 11-20, 4 21-30, 5 31-40, 6 >40 per week.

def glasses_to_band(n):
    """Map glasses per week onto the AlchlGlz band. Registry bands, verbatim."""
    if n is None or n < 0:
        return None
    if n == 0:
        return 0
    if n < 1:
        return 1
    if n <= 10:
        return 2
    if n <= 20:
        return 3
    if n <= 30:
        return 4
    if n <= 40:
        return 5
    return 6


def extract_alcohol(text):
    """-> (status on the `alcohol` scale or None, AlchlGlz band or None)."""
    t = norm(text)
    status = None
    if re.search(r"\b(?:geen alcohol|nooit alcohol|alcohol: nee|abstinent|geheelonthouder)\b", t):
        status = 0
    elif re.search(r"\b(?:gestopt met alcohol|voorheen alcohol|vroeger alcohol)\b", t):
        status = 1
    elif re.search(r"\b(?:drinkt|alcoholgebruik: ?ja|gebruikt alcohol|"
                   r"alcohol ?\+)\b", t) or re.search(
                   r"\d+\s*(?:glazen|glas|eenheden)", t):
        status = 3
    band = None
    m = re.search(r"(\d{1,3}(?:[.,]\d+)?)\s*(?:glazen|glas|eenheden|e\.?)\s*(?:per|/)\s*week", t)
    if m:
        band = glasses_to_band(_num(m.group(1)))
    else:
        m = re.search(r"(\d{1,2}(?:[.,]\d+)?)\s*(?:glazen|glas|eenheden)\s*(?:per|/)\s*dag", t)
        if m:
            v = _num(m.group(1))
            band = glasses_to_band(v * 7) if v is not None else None
        elif status == 0:
            band = 0
    return status, band


# ---------------------------------------------------------------- 5. onset year
#
# KliMaYr: "Jaar eerste uiting klin.manifest vaatlijden" -> the EARLIEST year mentioned
# in a vascular-event context. KliMaC's own value labels name the qualifying events, so
# the term list below is taken from them rather than invented: hartinfarct, hartstilstand,
# beroerte, aneurysma aorta, amputatie, CABG, PTCA/dotter, halsslagader-operatie,
# desobstructie, stent, beenvaten-operatie.

EVENT_TERMS = (r"(?:myocardinfarct|hartinfarct|infarct|mi\b|hartstilstand|"
               r"cabg|bypass|ptca|dotter|stent|pci\b|"
               r"cva|tia|beroerte|herseninfarct|"
               r"aneurysma|aaa\b|"
               r"endarteriectomie|desobstructie|halsslagader|carotisoperatie|"
               r"amputatie|claudicatio|revascularisatie|vaatoperatie)")
YEAR_WINDOW = 30
YEAR_MIN, YEAR_MAX = 1930, 2030
# A year that states WHEN something happened is introduced by one of these. A bare year
# with no cue is usually a document, letter or scan date -- which is what flooded the
# onset feature when --date-mode year converted full dates into years.
HISTORY_CUE = r"(?:in|sinds|sedert|anno|vanaf|rond|omstreeks)"


def extract_onset_years(text, require_cue=True):
    """-> list of plausible years mentioned next to a vascular event term.

    `require_cue` demands a temporal preposition immediately before the year, so that a
    date printed in a letterhead is not read as the year a disease began.
    """
    t = norm(text)
    out = []
    for m in re.finditer(r"\b(19\d{2}|20\d{2})\b", t):
        y = int(m.group(1))
        if not (YEAR_MIN <= y <= YEAR_MAX):
            continue
        if require_cue and not re.search(HISTORY_CUE + r"\s+$", t[:m.start()]):
            continue
        ctx = t[max(0, m.start() - YEAR_WINDOW):m.end() + YEAR_WINDOW]
        if re.search(EVENT_TERMS, ctx):
            out.append(y)
    return out


# ---------------------------------------------------------------- 6. aorta diameter
#
# aorta_hg: "Grootste diameter aorta (cm.) (echo)" -> the MAXIMUM, in centimetres.

AORTA_TERMS = r"(?:aorta|aneurysma|aaa\b|aortadiameter)"
# A bare length near the word "aorta" is not an aortic diameter. Requiring a measurement
# cue is what separates "aorta, diameter 4,2 cm" from "5 cm distaal van de aorta".
AORTA_CUE = r"(?:diameter|doorsnede|ap-?diameter|maximaal|max\.?|dia\b|wijdte|kaliber)"
AORTA_WINDOW = 30
AORTA_LEAD = 20      # chars in which the aorta term may NAME the object before the number


def extract_aorta_cm(text):
    """-> list of aortic diameters in cm, mm converted."""
    t = norm(text)
    out = []
    for m in re.finditer(r"(\d{1,3}(?:[.,]\d+)?)\s*(cm|mm)\b", t):
        v = _num(m.group(1))
        if v is None:
            continue
        cm = v / 10.0 if m.group(2) == "mm" else v
        ctx = t[max(0, m.start() - AORTA_WINDOW):m.end() + AORTA_WINDOW]
        if not re.search(AORTA_TERMS, ctx):
            continue
        lead = t[max(0, m.start() - AORTA_LEAD):m.start()]
        # Either a measurement cue, or the aorta named immediately before the number. A
        # term that only FOLLOWS the number is describing a location, not a diameter.
        if not (re.search(AORTA_CUE, ctx) or re.search(AORTA_TERMS, lead)):
            continue
        if 1.0 <= cm <= 12.0:      # an adult aorta outside this range is a parse error
            out.append(cm)
    return out


# ---------------------------------------------------------------- 7. medication classes
#
# ATC prefixes per SMART medication group. The GROUP definitions come from smart.csv's own
# labels; the ATC prefixes implementing them are standard WHO ATC and are NOT in the repo,
# so they are declared in ASSUMPTIONS.md #1. Drug NAMES are never written here: they are
# derived from the cohort's med_20250709.csv (med_ZIatc + med_genNaam).

MED_CLASSES = {
    # antihypertensives -- these are the groups mht_alln counts
    "betablokker":        {"atc": ("C07",),            "smart": "mht01"},
    "diureticum":         {"atc": ("C03",),            "smart": "mht02"},
    "ace_remmer":         {"atc": ("C09A", "C09B"),    "smart": "mht03"},
    "calciumantagonist":  {"atc": ("C08",),            "smart": "mht04"},
    "alfablokker":        {"atc": ("C02CA",),          "smart": "mht05"},
    "centraal_antihyp":   {"atc": ("C02A",),           "smart": "mht07"},
    "at1_antagonist":     {"atc": ("C09C", "C09D"),    "smart": "mht12"},
    "vasodilatator":      {"atc": ("C02DB", "C02DD"),  "smart": "mht41"},
    # lipid-lowering
    "statine":            {"atc": ("C10AA",),          "smart": "mli01"},
    "fibraat":            {"atc": ("C10AB",),          "smart": "mli02"},
    "galzuurbinder":      {"atc": ("C10AC",),          "smart": "mli03"},
    "cholesterolabsorptieremmer": {"atc": ("C10AX09",), "smart": "mli04"},
    # antithrombotics
    "plaatjesremmer":     {"atc": ("B01AC",),          "smart": "mas01"},
    "vka":                {"atc": ("B01AA",),          "smart": "mas02"},
    "lmwh":               {"atc": ("B01AB",),          "smart": "mas02c"},
    "doac":               {"atc": ("B01AE", "B01AF"),  "smart": "mas03"},
    # glucose-lowering
    "oraal_antidiabeticum": {"atc": ("A10B",),         "smart": "mgl01"},
    "insuline":           {"atc": ("A10A",),           "smart": "mgl02"},
}

# The subset mht_alln counts: "Aantal verschillende groepen antihypertensiva".
ANTIHYPERTENSIVE = tuple(k for k, v in MED_CLASSES.items() if v["smart"].startswith("mht"))


# Tokens in med_genNaam that are not drug names: ATC combination and salt wording.
# "ENALAPRIL AND DIURETICS" must contribute `enalapril`, not the phrase, which no letter
# ever writes.
_MED_STOPTOKENS = {
    # connectors, salts and ATC class wording
    "and", "acid", "human", "sparing", "agents", "potassium", "calcium", "sodium",
    "combinations", "other", "plain", "derivatives", "etexilate", "levorotatory",
    "diuretics", "antihypertensives", "preparations", "related", "atc",
    "in", "with", "or", "the",
}


def med_stems(name):
    """English INN from med_genNaam -> stems that also match the Dutch surface form.

    THIS IS THE FIX FOR THE ARM'S BIGGEST FAILURE. `med_genNaam` holds WHO/ATC **English**
    INN names, not the Dutch spellings clinicians write, so matching the values verbatim
    against Dutch narrative recovered almost nothing -- validated at sensitivity 0.001 for
    statins and 0.000 for insulin, while beta-blockers reached 0.265 purely because
    metoprolol/bisoprolol/atenolol happen to be spelled identically in both languages.
    That contrast is what identified the cause.

      SIMVASTATIN          -> Dutch simvastatine
      INSULIN GLARGINE     -> Dutch insuline glargine
      HEPARIN              -> Dutch heparine
      ACETYLSALICYLIC ACID -> Dutch acetylsalicylzuur

    So each token is reduced to a stem and matched as stem + any word characters, which
    covers the regular Dutch endings without inventing a translation table. The trims are
    morphological, not per-drug: a trailing 'e' (dipyridamole/dipyridamol) and a trailing
    'ic' (acetylsalicylic/acetylsalicylzuur). See ASSUMPTIONS.md #9.

    Stems are >= 6 characters, so a short fragment cannot match unrelated prose.

    Only the FIRST qualifying token is used -- the active substance. Trailing tokens are
    salts, insulin variants and ATC class wording, and taking them too produced exactly the
    false positives this arm cannot afford: "CARBASALATE CALCIUM" contributed the stem
    `calcium`, which matches "calciumantagonist" and any calcium lab value, and
    "INSULIN ASPART" contributed `aspart`, which matches "aspartaat" (the ASAT enzyme).
    """
    for tok in re.split(r"[^a-z]+", norm(name)):
        if len(tok) < 6 or tok in _MED_STOPTOKENS:
            continue
        if tok.endswith("ic"):
            tok = tok[:-2]
        elif tok.endswith("e"):
            tok = tok[:-1]
        return {tok} if len(tok) >= 6 else set()
    return set()


def compile_med_lexicon(lexicon):
    """{class: [INN names]} -> {class: compiled stem alternation}.

    Anchored at the start of a word, so a stem cannot match mid-word: the concept arm
    already read C=0.910 for smoking because `roken` matched "afgesproken". The trailing
    [a-z]* is what admits the Dutch ending.
    """
    out = {}
    for cls, names in lexicon.items():
        stems = set()
        for n in names or ():
            stems |= med_stems(n)
        if stems:
            toks = sorted(stems, key=len, reverse=True)
            out[cls] = re.compile(r"\b(?:" + "|".join(re.escape(x) for x in toks) + r")[a-z]*\b")
    return out


def extract_medications(text, compiled):
    """-> set of medication classes named in this text."""
    t = norm(text)
    return {cls for cls, rx in compiled.items() if rx.search(t)}


# ---------------------------------------------------------------- 8. the JOIN positive control
#
# WHY THIS IS HERE. After two rounds of extractor fixes, every graded feature still agreed
# with its curated counterpart at |rho| < 0.2, and the medication table showed the telling
# signature: for all 15 classes, sensitivity ~= 1 - specificity (mean difference +0.008).
# A weak-but-real detector has sens > 1-spec; these matches are statistically INDEPENDENT
# of whether the patient takes the drug. That is not a tuning problem, and it appeared
# across stenosis, smoking, alcohol, aorta and onset at the same time.
#
# Two explanations survive, and they have opposite consequences:
#   (a) the letters mention these facts non-specifically (boilerplate, advice, family
#       history), so per-patient extraction of them is simply not possible here;
#   (b) the documents are not joined to the right patients, in which case EVERY text arm
#       in this project is invalid -- T0 volume, T1 TF-IDF and T2 concepts included -- and
#       the free-text null measures a plumbing bug rather than the data.
#
# Note the concept arm's "clinically plausible prevalences" (diabetes 23.9%, smoking 39.4%)
# never distinguished these: a patient-shuffled cache preserves prevalence exactly. So that
# reassurance was not evidence of a correct join.
#
# Age and sex settle it. Both are stated in nearly every Dutch clinical letter, both are
# trivial to extract, and both have a curated counterpart that MUST agree if the join is
# right. This is the text arm's equivalent of the structured arm's positive control -- the
# check that made its 0.7576 interpretable.

SEX_MALE = r"\b(?:man|mannelijke?|meneer|dhr|heer)\b"
SEX_FEMALE = r"\b(?:vrouw|vrouwelijke?|mevrouw|patiente|dame)\b"
AGE_MIN, AGE_MAX = 18, 110


def extract_sex(text):
    """-> 1 (Man) / 2 (Vrouw) on `geslacht`'s own codes, or None.

    Codes are the registry's: smart.csv gives geslacht 1 -> Man, 2 -> Vrouw, 9 -> Missend.
    Whichever term occurs more often wins, since a letter may also mention a partner.
    """
    t = norm(text)
    m = len(re.findall(SEX_MALE, t))
    f = len(re.findall(SEX_FEMALE, t))
    if m == f:
        return None
    return 1 if m > f else 2


def extract_ages(text):
    """-> list of ages in years. A cue is required, so no bare number can qualify."""
    t = norm(text)
    out = []
    for pat in (r"(\d{2,3})\s*-?\s*jarige?\b", r"leeftijd\s*:?\s*(\d{2,3})\b",
                r"(?:man|vrouw|patiente?)\s+van\s+(\d{2,3})\s*jaar\b"):
        for mt in re.finditer(pat, t):
            v = int(mt.group(1))
            if AGE_MIN <= v <= AGE_MAX:
                out.append(v)
    return out


# ---------------------------------------------------------------- validation against curation
#
# The cheapest and most important check on this whole arm, and it never touches the outcome:
# for every extracted quantity there is a curated variable measuring the same thing on the
# same patients, so agreement can be measured directly. That converts "does the extraction
# work?" from an argument into a number -- and it is how ASSUMPTIONS.md #4's word-to-band
# mapping gets settled empirically rather than by my say-so.
#
# Sentinel missing-value codes are taken from smart.csv's own value labels ("Missend",
# "n.v.t.", "Onbeantwoord"), not guessed. Failing to mask them would compare an extracted
# grade against the number 9 and report near-zero agreement everywhere.

CURATED_MISSING = {
    "stenACIl": (9,), "stenACIr": (9,),          # 9 -> Missend
    "csten_50": (9,), "csten_70": (9,),          # 9 -> Missend
    "packyrs": (999,),                           # 999 -> Missend
    "roken": (9,), "alcohol": (9,),              # 9 -> Missend
    "AlchlGlz": (95, 98, 99),                    # Onbeantwoord / Niet van toepassing / Missend
    "KliMaYr": (9997, 9998, 9999),               # startjaar mist / operatiejaar mist / n.v.t.
    "aorta_hg": (99,), "AortDist": (99,), "AortProx": (99,),
    "mht_alln": (),                              # '.' only, already NaN after read_csv
    "nrfaln_n": (9,),
    "geslacht": (9,),                            # 9 -> Missend
    "leeftijd": (999,),                          # 999 -> Missend
}

# extracted feature -> (curated variable(s), comparison kind). `max` means the extracted
# value is compared against the larger of two curated sides.
VALIDATION_PAIRS = (
    # THE JOIN POSITIVE CONTROL -- read these two first. If they do not agree strongly,
    # the documents are not joined to the right patients and NOTHING below is
    # interpretable, nor is any earlier text arm.
    ("graded.sex_from_text", ("geslacht",), "categorical"),
    ("graded.age_from_text", ("leeftijd",), "numeric"),
    ("graded.stenosis_max", ("stenACIl", "stenACIr"), "ordinal_max"),
    ("graded.stenosis_left_max", ("stenACIl",), "ordinal"),
    ("graded.stenosis_right_max", ("stenACIr",), "ordinal"),
    ("graded.stenosis_ge50", ("csten_50",), "binary"),
    ("graded.stenosis_ge70", ("csten_70",), "binary"),
    ("graded.packyears", ("packyrs",), "numeric"),
    ("graded.packyears_stated", ("packyrs",), "numeric"),
    ("graded.smoking_status_last", ("roken",), "categorical"),
    ("graded.alcohol_status_last", ("alcohol",), "categorical"),
    ("graded.alcohol_glasses_band", ("AlchlGlz",), "ordinal"),
    ("graded.onset_year_min", ("KliMaYr",), "numeric"),
    ("graded.aorta_cm_max", ("aorta_hg",), "numeric"),
    ("graded.n_antihypertensive_classes", ("mht_alln",), "numeric"),
)


def _spearman(a, b):
    """Rank correlation, ties averaged. numpy only -- scipy is not a dependency here."""
    import numpy as np
    if len(a) < 8:
        return None

    def rank(x):
        order = np.argsort(x, kind="mergesort")
        r = np.empty(len(x), float)
        r[order] = np.arange(len(x), dtype=float)
        # average tied ranks, or a heavily tied ordinal scale reports a spurious value
        _, inv, cnt = np.unique(x, return_inverse=True, return_counts=True)
        sums = np.zeros(len(cnt))
        np.add.at(sums, inv, r)
        return (sums / cnt)[inv]

    ra, rb = rank(np.asarray(a, float)), rank(np.asarray(b, float))
    sa, sb = ra.std(), rb.std()
    if sa < 1e-12 or sb < 1e-12:
        return None
    return float(((ra - ra.mean()) * (rb - rb.mean())).mean() / (sa * sb))
