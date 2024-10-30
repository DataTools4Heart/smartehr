import numpy as np
import pandas as pd
from torch.utils.data import Dataset
import pandas as pd
from pycox.preprocessing import label_transforms
import random
import torch

smart_features_map = {
    "age": "leeftijd",
    "gender": "geslacht",  # 1 Male and 2 Female? or the opposite?
    "smoker": "roken",  # 0 non smoker, >=1 smoker?
    "systolic_blood_pressure": "bdsys",
    "diabetes": "vz_DM",  # Defined differently, 0 is no and 1 yes?
    "cad": "vz_hart",  # it says general cardiac disease vg_0321
    "cvd": "vz_kop",  # 0 no, 1 yes?
    "aaa": "vz_aaa",  # 0 no, 1 yes?
    "pad": "vz_been",  # It's vascular and not arterial
    "time_since_first_cd": "KliMaDur",  # "KliMaDur", #not sure
    "hdl_cholesterol": "labhdl",
    "total_cholesterol": "labchol",
    "egfr": "labkrea",  # Can this be considered standardized serum creatinine?
    "high_sens_crp": "labcrp",
}

smart_outcomes_map = {
    "death_time": "edood_f",
    "death_yesno": "edood_n",
    "death_vascular": "edoodvas",  # Vascular death is the same as cardio-vascular death?
    "stroke_time": "ebero_f",
    "stroke_yesno": "ebero_n",
    "stroke_type": "ebero_s",  # Codes for ischaemic and hemorrahagic strokes
    "myo_time": "emi_f",
    "myo_yesno": "emi_n",
    "myo_type": "emi_s",  # Which codes are good?
}


numeric_feature_ranges = {
    "age": [30, 100],
    "systolic_blood_pressure": [70, 200],
    "time_since_first_cd": [0, 30],
    "hdl_cholesterol": [0.6, 2.50],
    "total_cholesterol": [2.5, 8.0],
    "egfr": [30.0, 120.0],
    "high_sens_crp": [0.1, 15.0],
}


def egfr(scr: float, age: int, male: int):
    if scr == 0.0 or age == 0.0:
        return 0
    gender_f = 1.0 if male == 1 else 0.742
    egfr = 175 * (scr ** (-1.154)) * (age ** (-0.203)) * gender_f
    return egfr


def compute_first_cd_event(smart: pd.DataFrame):
    def compute_time(s: pd.Series):
        t = max([s[f"{event}_time"] for event in ["death", "stroke", "myo"]])  # OR cut-off date (censoring)
        times = [s[f"{event}_time"] for event in ["death", "stroke", "myo"] if s[event]]
        if times:
            t = min(times)
        return t

    target_stroke_types = [11, 102]
    target_myo_types = [41, 101]
    smart["death"] = smart.apply(lambda x: x["death_vascular"] > 0, axis=1)
    smart["stroke"] = smart.apply(lambda x: x["stroke_yesno"] > 0 and x["stroke_type"] in target_stroke_types, axis=1)
    smart["myo"] = smart.apply(lambda x: x["myo_yesno"] > 0 and x["myo_type"] in target_myo_types, axis=1)
    smart["cd_event"] = smart.apply(lambda x: x["death"] or x["stroke"] or x["myo"] in target_myo_types, axis=1)
    smart["cd_time"] = smart.apply(compute_time, axis=1)
    smart = smart.drop([k for k in smart_outcomes_map.keys()] + ["death", "stroke", "myo"], axis=1)
    return smart


def preprocess_smart(smart: pd.DataFrame):
    inverse_smart_features_map = {v: k for k, v in smart_features_map.items()}
    inverse_smart_outcomes_map = {v: k for k, v in smart_outcomes_map.items()}
    rename_dict = inverse_smart_features_map | inverse_smart_outcomes_map
    rename_dict = {k: v for k, v in rename_dict.items() if k in smart.columns}
    keys = [v for v in rename_dict.values()] + ["cd_event", "cd_time"]
    smart = smart.rename(columns=rename_dict).loc[:, keys]
    for feature, (min_val, max_val) in numeric_feature_ranges.items():
        if feature in smart.columns:
            smart[feature] = smart[feature].clip(lower=min_val, upper=max_val)

    smart["egfr"] = smart.apply(lambda x: egfr(x["egfr"] * 0.0113, x["age"], x["gender"]), axis=1)
    smart["smoker"] = smart["smoker"].apply(lambda x: 1 if x > 0 else 0)  # assuming non smoker == 0
    smart["age2"] = smart["age"] ** 2
    smart["egfr2"] = smart["egfr"] ** 2
    smart["log_high_sens_crp"] = np.log(smart["high_sens_crp"])
    return smart


class SMARTPoC(Dataset):
    def __init__(
        self,
        smart_string: pd.DataFrame,
        name_map: dict[str, str],
        labtrans: label_transforms.LabTransDiscreteTime,
    ) -> None:
        self.labtrans = labtrans
        self.durations, self.events = smart_string["cd_time"].values, smart_string["cd_event"].values
        if self.labtrans is not None:
            self.durations, self.events = self.labtrans.transform(self.durations, self.events)
        self.smart_string = smart_string.drop(["cd_time", "cd_event"], axis=1)
        self.name_map = name_map

    def __len__(self):
        return len(self.smart_string)

    def __getitem__(self, idx: int):
        features = {}
        for col in self.smart_string:
            features[col] = self.name_map[col] + self.smart_string[col].iloc[idx]
        return (
            features,
            self.durations[idx],
            self.events[idx],
        )


def collate_fn_smart_poc(batch, tokenizer):
    features, durations, events = [b[0] for b in batch], [b[1] for b in batch], [b[2] for b in batch]
    features = [[v for v in f.values()] for f in features]

    for i in range(len(features)):
        random.shuffle(features[i])
        features[i] = "<sep>".join(features[i])

    encodings = tokenizer.encode_batch(features)
    ids = torch.stack([torch.tensor(e.ids) for e in encodings])
    masks = ~torch.stack([torch.tensor(e.attention_mask, dtype=torch.bool) for e in encodings])

    return (
        {"input_ids": ids, "padding_mask": masks},
        torch.tensor(durations),
        torch.tensor(events),
    )
