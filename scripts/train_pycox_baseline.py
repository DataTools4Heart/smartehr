import init
from pycox_utils.utils import (
    load_pycox_model,
    discrete_label_transform,
    eval_pycox,
)
from pycox.models.cox_time import MLPVanillaCoxTime
from dataset_utils.utils import load_for_pycox
import torchtuples as tt
import matplotlib.pyplot as plt
import hydra
from config.config import Config
from config.model.model import PycoxModelParams
from config.training.training import PycoxTrainingParams


@hydra.main(version_base=None, config_path="../config", config_name="config")
def train_and_evaluate_pycox_model_for_smart(cfg: Config):
    model_params = PycoxModelParams(**cfg.model)
    train_params = PycoxTrainingParams(**cfg.training)
    dataset_params = cfg.dataset
    data_dict = load_for_pycox(dataset_params)
    x_train, y_train, x_val, y_val, x_test, y_test = (
        data_dict["x_train"],
        data_dict["y_train"],
        data_dict["x_val"],
        data_dict["y_val"],
        data_dict["x_test"],
        data_dict["y_test"],
    )
    evaluation_times, num_intervals = data_dict["evaluation_times"], data_dict["num_intervals"]

    model_cls, label_transform, is_discrete = load_pycox_model(model_params.name)
    if is_discrete or model_params.name == "pc_hazard":
        y_train, y_val, labtrans = discrete_label_transform(y_train, y_val, label_transform, num_intervals)
        out_features = labtrans.out_features
    elif label_transform is not None:
        labtrans = label_transform()
        y_train = labtrans.fit_transform(*y_train)
        y_val = labtrans.transform(*y_val)
    in_features = x_train.shape[1]
    out_features = labtrans.out_features if label_transform is not None else 1

    if model_params.name == "cox_time":
        net = MLPVanillaCoxTime(
            in_features,
            model_params.num_nodes,
            model_params.batch_norm,
            model_params.dropout,
        )
    else:
        net = tt.practical.MLPVanilla(
            in_features,
            model_params.num_nodes,
            out_features,
            model_params.batch_norm,
            model_params.dropout,
            output_bias=model_params.output_bias,
        )
    if is_discrete or model_params.name == "pc_hazard":
        model = model_cls(net, tt.optim.Adam, duration_index=labtrans.cuts, device=train_params.device)
    else:
        model = model_cls(net, tt.optim.Adam, device=train_params.device)
    if train_params.lr is None:
        lrfinder = model.lr_finder(x_train.values, y_train, train_params.batch_size, tolerance=10)
        lr = lrfinder.get_best_lr()
    else:
        lr = train_params.lr

    model.optimizer.set_lr(lr)
    callbacks = [tt.callbacks.EarlyStopping(patience=train_params.patience)]
    verbose = False
    log = model.fit(
        x_train.values,
        y_train,
        train_params.batch_size,
        train_params.epochs,
        callbacks,
        verbose,
        val_data=(x_val.values, y_val),
        val_batch_size=train_params.batch_size,
    )

    fig = plt.figure()
    plt.plot(log.to_pandas())
    fig.savefig("learning_curve.png")

    if not is_discrete and model_params.name != "pc_hazard":
        model.compute_baseline_hazards()
    roc, ci = eval_pycox(model, x_test, y_test, is_discrete, evaluation_times)
    print("ROC AUC:", roc)
    print("CI:", ci)


if __name__ == "__main__":
    train_and_evaluate_pycox_model_for_smart()
