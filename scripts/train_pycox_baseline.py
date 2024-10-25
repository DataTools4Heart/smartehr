import init
from pycox_utils.utils import (
    PyCoxBaselineParams,
    load_pycox_model,
    prepare_data_for_training,
    discrete_label_transform,
    eval_pycox,
)
from argparse import ArgumentParser
from omegaconf import OmegaConf
from pycox.models.cox_time import MLPVanillaCoxTime
import torchtuples as tt
import matplotlib.pyplot as plt


def train_and_evaluate_pycox_model_for_smart(
    params: PyCoxBaselineParams,
):
    model_params = params.model_params
    train_params = params.train_params
    dataset_params = params.dataset_params
    data_dict = prepare_data_for_training(dataset_params)
    x_train, y_train, x_val, y_val, x_test, y_test = (
        data_dict["x_train"],
        data_dict["y_train"],
        data_dict["x_val"],
        data_dict["y_val"],
        data_dict["x_test"],
        data_dict["y_test"],
    )
    evaluation_times, num_intervals = data_dict["evaluation_times"], data_dict["num_intervals"]

    model_cls, label_transform, is_discrete = load_pycox_model(model_params.model_name)
    if is_discrete or model_params.model_name == "pc_hazard":
        y_train, y_val, labtrans = discrete_label_transform(y_train, y_val, label_transform, num_intervals)
        out_features = labtrans.out_features
    elif label_transform is not None:
        labtrans = label_transform()
        y_train = labtrans.fit_transform(*y_train)
        y_val = labtrans.transform(*y_val)
    in_features = x_train.shape[1]
    out_features = labtrans.out_features if label_transform is not None else 1

    if model_params.model_name == "cox_time":
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
    if is_discrete or model_params.model_name == "pc_hazard":
        model = model_cls(net, tt.optim.Adam, duration_index=labtrans.cuts, device=train_params.device)
    else:
        model = model_cls(net, tt.optim.Adam, device=train_params.device)
    lrfinder = model.lr_finder(x_train.values, y_train, train_params.batch_size, tolerance=10)
    lr = lrfinder.get_best_lr()

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

    if not is_discrete and model_params.model_name != "pc_hazard":
        model.compute_baseline_hazards()
    roc, ci = eval_pycox(model, x_test, y_test, is_discrete, evaluation_times)
    print("ROC AUC:", roc)
    print("CI:", ci)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--cfg-path", type=str, required=True)
    args = parser.parse_args()
    cfg_path = args.cfg_path
    with open(cfg_path, "r") as f:
        yaml_conf = OmegaConf.to_container(OmegaConf.load(f), resolve=True)
        params = PyCoxBaselineParams(**yaml_conf)
    train_and_evaluate_pycox_model_for_smart(params)
