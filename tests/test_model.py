"""
tests/test_model.py

Smoke test: does the full pipeline (feature selection -> engineered
features -> preprocessing -> training -> prediction -> evaluation) run
end-to-end without raising, on a small synthetic dataset shaped like
the real one? This is not a correctness test on real clinical data —
it exists to prove the pipeline breaks loudly if something upstream
changes shape or a required column goes missing, not to prove
predictive quality.
"""

import numpy as np
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split

from src.data import build_model_dataframe, select_features, split_features_and_target
from src.features import add_engineered_features, get_engineered_feature_names
from src.model import build_pinned_model, build_pipeline, evaluate_model, predict_with_timing, train_model


@pytest.fixture
def synthetic_dataset():
    """~50-row synthetic dataset mirroring the real dataset's schema."""
    rng = np.random.RandomState(42)
    n = 50

    df = pd.DataFrame({
        "age": rng.randint(1, 95, size=n),
        "hr": rng.randint(50, 160, size=n),
        "sbp": rng.randint(70, 180, size=n),
        "dbp": rng.randint(40, 110, size=n),
        "rr": rng.randint(10, 35, size=n),
        "o2sat": rng.randint(85, 100, size=n),
        "temp": rng.uniform(35.5, 40.0, size=n),
        "arrival_mode": rng.choice(["walk-in", "ambulance"], size=n),
        "cc_chest_pain": rng.randint(0, 2, size=n),
        "cc_fever": rng.randint(0, 2, size=n),
        "esi": rng.choice([1, 2, 3, 4, 5], size=n, p=[0.05, 0.15, 0.4, 0.3, 0.1]),
    })
    return df


def test_training_pipeline_runs_end_to_end_on_small_sample(synthetic_dataset):
    """
    Full pipeline smoke test: given ~50 synthetic rows, feature
    selection, engineered features, preprocessing, training and
    evaluation should all run without raising, and produce a
    prediction for every test-set row plus every expected metric key.
    """
    df = add_engineered_features(synthetic_dataset)
    engineered_names = get_engineered_feature_names(synthetic_dataset)

    selected_features = select_features(df) + engineered_names
    model_df = build_model_dataframe(df, selected_features, target="esi")
    X, y = split_features_and_target(model_df, target="esi")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    numeric_features = X.select_dtypes(include="number").columns.tolist()
    categorical_features = X.select_dtypes(exclude="number").columns.tolist()

    estimator = build_pinned_model(max_iter=200, class_weight="balanced", random_state=42)
    pipeline = build_pipeline(numeric_features, categorical_features, estimator)

    pipeline, train_time = train_model(pipeline, X_train, y_train)
    predictions, inference_ms = predict_with_timing(pipeline, X_test)

    assert len(predictions) == len(y_test)
    assert train_time >= 0
    assert inference_ms >= 0

    metrics = evaluate_model(y_test, predictions)
    for key in ("accuracy", "precision_macro", "recall_macro", "f1_macro", "f1_weighted"):
        assert key in metrics
        assert 0.0 <= metrics[key] <= 1.0


def test_engineered_features_are_added(synthetic_dataset):
    """shock_index and pulse_pressure should be added when hr/sbp/dbp are present."""
    df = add_engineered_features(synthetic_dataset)
    assert "shock_index" in df.columns
    assert "pulse_pressure" in df.columns
    assert (df["pulse_pressure"] == df["sbp"] - df["dbp"]).all()
