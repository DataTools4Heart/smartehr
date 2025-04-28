from models import weighted_lstm, tann


def apply_transforms(train, val, test, model_name: str):
    if model_name == "weighted_lstm":
        train = train.with_transform(weighted_lstm.tensorize_features)
        val = val.with_transform(weighted_lstm.tensorize_features)
        test = test.with_transform(weighted_lstm.tensorize_features)
    elif model_name == "tann":
        train = train.with_transform(tann.tensorize_features)
        val = val.with_transform(tann.tensorize_features)
        test = test.with_transform(tann.tensorize_features)
    return train, val, test
