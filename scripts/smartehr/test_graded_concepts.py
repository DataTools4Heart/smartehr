"""Fixtures for the graded/medication extractors. Run: python test_graded_concepts.py

No real clinical text is used or needed: every case below is written to exercise one
decision, including the ways an extractor can invent a value that is not there. The
structured arm's history is the reason this file exists -- `gfr_count` read C=0.851 as a
pure missingness artefact, and `roken` read 0.910 by matching "afgesproken" -- so a
plausible-looking number from a text extractor is assumed wrong until a fixture pins it.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from graded_concepts import (compile_med_lexicon, extract_alcohol, extract_aorta_cm,
                             extract_medications, extract_onset_years, extract_packyears,
                             extract_smoking_status, extract_stenosis, glasses_to_band,
                             pct_to_grade)

FAILED = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}\n{'' if ok else f'         got {got!r}, want {want!r}'}")
    if not ok:
        FAILED.append(label)


print("--- stenosis: percentages map through the registry's own bands (stenACI* 0-7) ---")
# The band edges are the ones smart.csv states: 0 / <=29 / 30-49 / 50-69 / >=70.
for pct, want in [(0, 0), (20, 1), (29, 1), (30, 2), (49, 2), (50, 3), (69, 3), (70, 4), (95, 4)]:
    check(f"{pct}% -> grade {want}", pct_to_grade(pct), want)
check("impossible percentage rejected", pct_to_grade(140), None)

print("\n--- stenosis: extraction from prose ---")
check("quantitative + side",
      extract_stenosis("Duplex: stenose van de ACI links van 65%."), [(3, "left")])
check("range coded by its upper bound (50-69% is band 3)",
      extract_stenosis("ACI rechts: stenose 50-69%."), [(3, "right")])
check("severe qualitative, no number",
      extract_stenosis("Ernstige stenose van de rechter carotis."), [(4, "right")])
check("occlusion",
      extract_stenosis("Occlusie van de ACI links."), [(6, "left")])
check("explicit absence is grade 0, not missing",
      extract_stenosis("Geen stenose of plaque in de carotiden."), [(0, None)])
# The failure that matters most: a percentage that has nothing to do with a stenosis.
check("stray percentage near no vessel term is ignored",
      extract_stenosis("Bij 70% van de patienten treedt dit op."), [])
check("percentage with a vessel but no stenosis term is ignored",
      extract_stenosis("De carotis is 70% van de referentiediameter afgebeeld."), [])
check("bilateral / unstated side is kept side-agnostic",
      extract_stenosis("Stenose van de carotiden beiderzijds, 80%."), [(4, None)])
# Regression: "occlusie" IS the lesion, so it has no stenosis noun to sit beside. An
# earlier version required adjacency for every severity word and scored this as nothing.
check("standalone lesion term needs no stenosis noun (regression)",
      extract_stenosis("Afsluiting van de linker carotis."), [(6, "left")])
check("pre-occlusive is 7, not 6 (its pattern contains the other's)",
      extract_stenosis("Pre-occlusieve ACI rechts."), [(7, "right")])

print("\n--- pack-years: packyrs = packs (of 20) per day x years ---")
check("stated pack-years", extract_packyears("Roken: 30 pakjaren."), [30.0])
check("English form", extract_packyears("40 pack-years."), [40.0])
check("Dutch decimal comma", extract_packyears("22,5 pakjaren"), [22.5])
# Regression: the trailing \b failed against the plural, so "pack-years" scored nothing
# while "pack-year" worked.
check("plural English form (regression)", extract_packyears("35 pack-years"), [35.0])
check("no-hyphen form", extract_packyears("35 packyears"), [35.0])
check("reconstructed from cigarettes/day x years (20/pack)",
      extract_packyears("Rookt 20 sigaretten per dag sinds 30 jaar."), [30.0])
check("reconstructed from packs/day",
      extract_packyears("2 pakjes per dag, gedurende 10 jaar."), [20.0])
# Refusing to invent the missing half is the point: a rate alone is not a pack-year count.
check("rate without a duration invents nothing",
      extract_packyears("Rookt 20 sigaretten per dag."), [])
check("a stated figure wins over reconstruction",
      extract_packyears("15 pakjaren; rookt 20 sigaretten per dag sinds 30 jaar."), [15.0])

print("\n--- smoking status on the `roken` scale (0 nooit, 1 vroeger, 3 momenteel) ---")
check("never", extract_smoking_status("Patient heeft nooit gerookt."), 0)
# 'ex-roker' contains 'roker' and 'gestopt met roken' contains 'roken': if the current
# pattern were tested first, every ex-smoker would be coded as a current smoker.
check("ex-smoker is 1, not 3", extract_smoking_status("Bekend ex-roker."), 1)
check("stopped smoking is 1, not 3",
      extract_smoking_status("Is gestopt met roken in 2010."), 1)
check("current", extract_smoking_status("Rookt nog steeds."), 3)
check("no mention -> None", extract_smoking_status("Geen bijzonderheden."), None)

print("\n--- alcohol: `alcohol` status and AlchlGlz bands ---")
for n, want in [(0, 0), (0.5, 1), (1, 2), (10, 2), (11, 3), (20, 3), (21, 4), (35, 5), (60, 6)]:
    check(f"{n} glasses/week -> band {want}", glasses_to_band(n), want)
check("glasses per week", extract_alcohol("Alcohol: 14 glazen per week."), (3, 3))
check("per day is converted to per week", extract_alcohol("Drinkt 2 eenheden per dag."), (3, 3))
check("abstinent -> status 0 band 0", extract_alcohol("Geen alcohol."), (0, 0))

print("\n--- onset year: KliMaYr is the EARLIEST year in a vascular context ---")
check("earliest of several events",
      min(extract_onset_years("Myocardinfarct in 2003, PTCA in 2011.")), 2003)
check("year with no event term nearby is ignored",
      extract_onset_years("Brief verzonden in 2015 naar de huisarts."), [])
check("implausible year rejected", extract_onset_years("infarct in 1850"), [])

print("\n--- aorta diameter: aorta_hg is the LARGEST, in cm ---")
check("cm", extract_aorta_cm("Aorta met een diameter van 5,5 cm."), [5.5])
check("mm converted to cm", extract_aorta_cm("Aneurysma, 48 mm."), [4.8])
check("length with no aorta term is ignored", extract_aorta_cm("Litteken van 5 cm."), [])
check("out-of-range value rejected", extract_aorta_cm("aorta 90 cm"), [])

print("\n--- medications: lexicon is data-derived, matching is word-bounded ---")
# Stands in for what the med CSV yields per ATC prefix.
lex = {"statine": ["Simvastatine", "Atorvastatine"],
       "betablokker": ["Metoprolol"],
       "ace_remmer": ["Enalapril"],
       "plaatjesremmer": ["Clopidogrel", "Acetylsalicylzuur"]}
cx = compile_med_lexicon(lex)
check("two classes found",
      extract_medications("Medicatie: simvastatine 40mg, metoprolol 50mg.", cx),
      {"statine", "betablokker"})
check("accent/case insensitive", extract_medications("ATORVASTATINE", cx), {"statine"})
# Word boundaries again: a substring match would fire inside an unrelated longer word.
check("substring inside another word does not match",
      extract_medications("premetoprololachtig", cx), set())
check("nothing found -> empty", extract_medications("Geen medicatie.", cx), set())

# ---------------------------------------------------------------- per-patient assembly
# Needs pandas/numpy and the builder module; skipped where they are unavailable so the
# extractor fixtures above still run anywhere.
try:
    import pandas as pd  # noqa: F401
    from prepare_text_features import graded_features
except Exception as e:                                          # pragma: no cover
    print(f"\n--- per-patient assembly: SKIPPED ({type(e).__name__}) ---")
else:
    print("\n--- per-patient assembly: aggregation follows each registry definition ---")
    lex = {"statine": ["Simvastatine"], "betablokker": ["Metoprolol"],
           "ace_remmer": ["Enalapril"], "diureticum": ["Hydrochloorthiazide"],
           "plaatjesremmer": ["Acetylsalicylzuur"]}
    cx = compile_med_lexicon(lex)
    pids = [1, 2, 3, 4]
    docs = {
        1: [(-800, "duplex: geringe stenose aci links. rookt 20 sigaretten per dag sinds 30 jaar."),
            (-100, "duplex: stenose aci links 80%. medicatie: metoprolol, simvastatine, "
                   "enalapril. myocardinfarct in 1998, cabg 2004. aorta 4,2 cm.")],
        2: [(-50, "geen stenose of plaque in de carotiden. ex-roker, 15 pakjaren. "
                  "medicatie: acetylsalicylzuur.")],
        3: [(-10, "patient komt voor controle. geen bijzonderheden.")],
        99: [(-10, "stenose aci rechts 90%")],          # not in the cohort
    }
    X = graded_features(docs, pids, cx, lambda *a: None)

    def g(row, col):
        return X.at[row, col]

    def nan_check(label, got):
        check(label, got != got, True)         # NaN is the only value not equal to itself

    check("worst grade wins (80% over an earlier 29%)", g(0, "graded.stenosis_max"), 4.0)
    check("last grade is the most recent document's", g(0, "graded.stenosis_last"), 4.0)
    check("csten_70 threshold derived from the grade", g(0, "graded.stenosis_ge70"), 1.0)
    check("pack-years reconstructed across documents", g(0, "graded.packyears"), 30.0)
    # KliMaYr is the FIRST manifestation, so 1998 rather than the later CABG in 2004.
    check("onset is the EARLIEST year, not the latest", g(0, "graded.onset_year_min"), 1998.0)
    # mht_alln counts antihypertensive groups only: metoprolol + enalapril = 2. The statin
    # is a lipid class (mli01) and must not be counted.
    check("antihypertensive count excludes the statin",
          g(0, "graded.n_antihypertensive_classes"), 2.0)
    check("total medication classes counts all three", g(0, "graded.n_med_classes"), 3.0)
    check("aorta takes the largest, in cm", g(0, "graded.aorta_cm_max"), 4.2)
    check("explicit absence is grade 0", g(1, "graded.stenosis_max"), 0.0)
    check("ex-smoker is 1", g(1, "graded.smoking_status_last"), 1.0)
    check("antiplatelet is not an antihypertensive",
          g(1, "graded.n_antihypertensive_classes"), 0.0)
    # The distinction that made gfr_count read C=0.851 in the structured arm: a patient
    # whose notes never mention stenosis has not been graded 0, they were not measured.
    nan_check("never-mentioned quantity is NaN, not 0", g(2, "graded.stenosis_max"))
    check("...but its _measured indicator is a real 0", g(2, "graded.stenosis_measured"), 0.0)
    # A patient with NO documents is different again: nothing was read, so even the
    # indicators are unknown and the pre-imputation screen should skip them.
    nan_check("patient with no documents stays all-NaN", g(3, "graded.stenosis_measured"))

print("\n" + ("ALL PASS" if not FAILED else f"{len(FAILED)} FAILURES: {FAILED}"))
sys.exit(1 if FAILED else 0)
