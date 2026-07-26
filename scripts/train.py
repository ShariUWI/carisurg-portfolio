"""
scripts/train.py

Entry point for training the pinned Phase 3 model (logistic
regression) from a single config file.

Usage
-----
    python scripts/train.py --config config.yaml

This script is intentionally the only place in the project where
side effects (file I/O, printing, saving artefacts) happen at the top
level — everything it calls into (src.data, src.features, src.model,
src.utils) is import-safe with no side effects of its own.
"""

import argparse
import json
import sys
from pathlib import Path

# Allow running as `python scripts/train.py` from the repo root without
# installing the project as a package.
sys.path.append(str(Path(__file__).resolve().parent.parent))

import joblib
from sklearn.model_selection import train_test_split

from src.data import (
    build_model_dataframe,
    check_leakage,
    select_features,
    split_features_and_target,
)
from src.features import add_engineered_features, get_engineered_feature_names
from src.model import build_pinned_model, build_pipeline, evaluate_model, predict_with_timing, train_model
from src.utils import load_config, set_random_seed
from src.data import load_dataset


def parse_args():
    parser = argparse.ArgumentParser(description="Train the pinned Phase 3 ED triage model.")
    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to the YAML config file (default: config.yaml).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    config = load_config(args.config)

    seed = set_random_seed(config["random_seed"])
    print(f"Random seed set to {seed}.")

    print(f"Loading dataset from {config['data']['path']} ...")
    df = load_dataset(config["data"]["path"], index_col=config["data"].get("index_col", 0))
    print(f"Loaded {df.shape[0]:,} rows, {df.shape[1]:,} columns.")

    leaked_columns = check_leakage(df)
    print(f"Potential leakage columns confirmed excluded: {leaked_columns}")

    if config.get("engineered_features", {}).get("enabled", False):
        ef_config = config["engineered_features"]
        df = add_engineered_features(
            df,
            hr_col=ef_config.get("hr_col", "hr"),
            sbp_col=ef_config.get("sbp_col", "sbp"),
            dbp_col=ef_config.get("dbp_col", "dbp"),
        )
        engineered_names = get_engineered_feature_names(
            df,
            hr_col=ef_config.get("hr_col", "hr"),
            sbp_col=ef_config.get("sbp_col", "sbp"),
            dbp_col=ef_config.get("dbp_col", "dbp"),
        )
        print(f"Engineered features added: {engineered_names}")
    else:
        engineered_names = []

    selected_features = select_features(df) + engineered_names
    target = config["data"]["target"]

    model_df = build_model_dataframe(df, selected_features, target)
    X, y = split_features_and_target(model_df, target)
    print(f"Modelling frame: {X.shape[0]:,} rows, {X.shape[1]} features.")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config["split"]["test_size"],
        stratify=y if config["split"].get("stratify", True) else None,
        random_state=config["split"]["random_state"],
    )
    print(f"Train/test split: {X_train.shape[0]:,} / {X_test.shape[0]:,} rows.")

    numeric_features = X.select_dtypes(include="number").columns.tolist()
    categorical_features = X.select_dtypes(exclude="number").columns.tolist()

    hp = config["model"]["hyperparameters"]
    estimator = build_pinned_model(
        max_iter=hp["max_iter"],
        class_weight=hp["class_weight"],
        random_state=hp["random_state"],
    )
    pipeline = build_pipeline(
        numeric_features,
        categorical_features,
        estimator,
        scale_numeric=config["model"].get("scale_numeric", True),
    )

    pipeline, train_time = train_model(pipeline, X_train, y_train)
    print(f"Training complete in {train_time:.2f}s.")

    predictions, inference_ms = predict_with_timing(pipeline, X_test)
    metrics = evaluate_model(y_test, predictions)
    metrics["training_time_seconds"] = train_time
    metrics["inference_time_ms_per_prediction"] = inference_ms

    print("Evaluation metrics:")
    print(f"  Accuracy:          {metrics['accuracy']:.3f}")
    print(f"  Precision (macro): {metrics['precision_macro']:.3f}")
    print(f"  Recall (macro):    {metrics['recall_macro']:.3f}")
    print(f"  F1 (macro):        {metrics['f1_macro']:.3f}")
    print(f"  Training time:     {train_time:.2f}s")
    print(f"  Inference time:    {inference_ms:.4f} ms/prediction")

    model_path = Path(config["output"]["model_path"])
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

    metrics_path = Path(config["output"]["metrics_path"])
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    with open(metrics_path, "w") as f:
        json.dump({k: v for k, v in metrics.items() if k != "report"}, f, indent=2)
    print(f"Metrics saved to {metrics_path}")


if __name__ == "__main__":
    main()
