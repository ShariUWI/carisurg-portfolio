"""
src/model.py

Preprocessing, training and evaluation functions for the ED triage
ESI prediction project.

Refactored from the Week 6 / Week 7 notebooks. The pinned Phase 3
model is logistic regression (see docs/decisions/2026-week-7-model-choice.md
for the reasoning) — `build_pinned_model()` constructs it directly from
config-style keyword arguments so scripts/train.py never has to know
about sklearn internals.

Nothing in this module has side effects at import time.
"""

import time
from typing import Iterable, Optional

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_preprocessor(
    numeric_features: Iterable[str],
    categorical_features: Iterable[str],
    scale_numeric: bool = True,
) -> ColumnTransformer:
    """
    Build a preprocessing ColumnTransformer: median imputation for
    numeric features (optionally followed by standard scaling), and
    most-frequent imputation + one-hot encoding for categorical
    features.

    Parameters
    ----------
    numeric_features : Iterable[str]
        Names of numeric predictor columns.
    categorical_features : Iterable[str]
        Names of categorical predictor columns.
    scale_numeric : bool, default True
        Whether to standard-scale numeric features after imputation.
        Logistic regression needs this; tree-based models do not.

    Returns
    -------
    ColumnTransformer
        Unfitted preprocessing transformer.
    """
    numeric_steps = [("imputer", SimpleImputer(strategy="median"))]
    if scale_numeric:
        numeric_steps.append(("scaler", StandardScaler()))
    numeric_pipeline = Pipeline(numeric_steps)

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    return ColumnTransformer([
        ("numeric", numeric_pipeline, list(numeric_features)),
        ("categorical", categorical_pipeline, list(categorical_features)),
    ])


def build_pinned_model(
    max_iter: int = 2000,
    class_weight: str = "balanced",
    random_state: int = 42,
) -> LogisticRegression:
    """
    Construct the Week 7 pinned Phase 3 model: logistic regression.

    Hyperparameters default to the values committed in config.yaml.
    Pass different values explicitly to override them (e.g. for a
    unit test), but config.yaml is the source of truth for production
    training via scripts/train.py.

    Parameters
    ----------
    max_iter : int, default 2000
    class_weight : str, default "balanced"
    random_state : int, default 42

    Returns
    -------
    LogisticRegression
        Unfitted estimator.
    """
    return LogisticRegression(
        max_iter=max_iter,
        class_weight=class_weight,
        random_state=random_state,
    )


def build_pipeline(
    numeric_features: Iterable[str],
    categorical_features: Iterable[str],
    estimator,
    scale_numeric: bool = True,
) -> Pipeline:
    """
    Assemble a full preprocessing + model pipeline.

    Parameters
    ----------
    numeric_features, categorical_features : Iterable[str]
        See `build_preprocessor`.
    estimator : sklearn-compatible estimator
        An unfitted classifier, e.g. the output of `build_pinned_model`.
    scale_numeric : bool, default True
        See `build_preprocessor`.

    Returns
    -------
    Pipeline
        Unfitted pipeline: preprocessor -> model.
    """
    preprocessor = build_preprocessor(numeric_features, categorical_features, scale_numeric)
    return Pipeline([("preprocessor", preprocessor), ("model", estimator)])


def train_model(pipeline: Pipeline, X_train: pd.DataFrame, y_train: pd.Series):
    """
    Fit a pipeline and time how long training takes.

    Parameters
    ----------
    pipeline : Pipeline
        Unfitted pipeline, e.g. from `build_pipeline`.
    X_train : pd.DataFrame
    y_train : pd.Series

    Returns
    -------
    tuple[Pipeline, float]
        (fitted_pipeline, training_time_seconds)
    """
    start = time.perf_counter()
    pipeline.fit(X_train, y_train)
    elapsed = time.perf_counter() - start
    return pipeline, elapsed


def predict_with_timing(pipeline: Pipeline, X_test: pd.DataFrame):
    """
    Predict on a test set and time batch inference.

    Parameters
    ----------
    pipeline : Pipeline
        A fitted pipeline.
    X_test : pd.DataFrame

    Returns
    -------
    tuple[np.ndarray, float]
        (predictions, batch_inference_ms_per_prediction)
    """
    start = time.perf_counter()
    predictions = pipeline.predict(X_test)
    elapsed = time.perf_counter() - start
    ms_per_prediction = (elapsed / len(X_test)) * 1000 if len(X_test) > 0 else float("nan")
    return predictions, ms_per_prediction


def evaluate_model(y_true: pd.Series, y_pred: np.ndarray) -> dict:
    """
    Compute headline classification metrics for a set of predictions.

    Parameters
    ----------
    y_true : pd.Series
        True target labels.
    y_pred : np.ndarray
        Predicted labels, same length and order as y_true.

    Returns
    -------
    dict
        Keys: accuracy, precision_macro, recall_macro, f1_macro,
        f1_weighted, and the full sklearn classification_report as a
        nested dict under "report".
    """
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)

    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_macro": report["macro avg"]["precision"],
        "recall_macro": report["macro avg"]["recall"],
        "f1_macro": report["macro avg"]["f1-score"],
        "f1_weighted": report["weighted avg"]["f1-score"],
        "report": report,
    }
