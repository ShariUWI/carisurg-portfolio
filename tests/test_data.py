"""
tests/test_data.py

Sanity check: does src.data produce the expected schema from a small,
synthetic frame shaped like the real dataset? This does not require
the real (programme-controlled) dataset — it is designed to break
loudly if the feature-selection or cleaning logic silently changes
behaviour.
"""

import numpy as np
import pandas as pd
import pytest

from src.data import (
    build_model_dataframe,
    check_leakage,
    get_arrival_features,
    get_chief_complaint_features,
    get_demographic_features,
    get_vital_features,
    select_features,
    split_features_and_target,
)


@pytest.fixture
def synthetic_raw_df():
    """A small synthetic frame mirroring the real dataset's schema."""
    return pd.DataFrame({
        "age": [25, 40, 63, 71, 19],
        "hr": [88, 102, 130, 95, 76],
        "sbp": [120, 90, 80, 110, 118],
        "dbp": [80, 60, 50, 70, 76],
        "rr": [16, 22, 28, 18, 14],
        "o2sat": [98, 94, 88, 96, 99],
        "temp": [37.0, 38.5, 39.2, 37.1, 36.8],
        "arrival_mode": ["walk-in", "ambulance", "ambulance", "walk-in", "walk-in"],
        "cc_chest_pain": [0, 1, 1, 0, 0],
        "cc_fever": [0, 0, 1, 0, 0],
        "gender": ["F", "M", "M", "F", "F"],  # deliberately not a predictor
        "disposition": ["home", "admit", "icu", "home", "home"],  # leakage column
        "esi": [4, 2, 1, 3, 5],
    })


def test_select_features_excludes_leakage_and_demographics(synthetic_raw_df):
    """
    select_features() should return only the intended predictor
    groups (age, vitals, arrival, chief complaint) — never the
    disposition/leakage column, and never demographic columns other
    than age.
    """
    features = select_features(synthetic_raw_df)

    assert "disposition" not in features
    assert "gender" not in features
    assert "age" in features
    assert "hr" in features
    assert "sbp" in features
    assert "arrival_mode" in features
    assert "cc_chest_pain" in features
    assert "cc_fever" in features
    # No duplicates
    assert len(features) == len(set(features))


def test_check_leakage_flags_disposition(synthetic_raw_df):
    leaked = check_leakage(synthetic_raw_df)
    assert "disposition" in leaked


def test_build_model_dataframe_drops_missing_target():
    df = pd.DataFrame({
        "age": [25, 40, 63],
        "hr": [88, 102, 130],
        "esi": [4, np.nan, 1],
    })
    model_df = build_model_dataframe(df, selected_features=["age", "hr"], target="esi")

    assert model_df.shape[0] == 2
    assert model_df["esi"].dtype == int
    assert list(model_df.columns) == ["age", "hr", "esi"]


def test_split_features_and_target_shapes(synthetic_raw_df):
    features = select_features(synthetic_raw_df)
    model_df = build_model_dataframe(synthetic_raw_df, features, target="esi")
    X, y = split_features_and_target(model_df, target="esi")

    assert "esi" not in X.columns
    assert len(X) == len(y)
    assert set(y.unique()).issubset({1, 2, 3, 4, 5})


@pytest.mark.parametrize(
    "helper, expected_hit",
    [
        (get_vital_features, "hr"),
        (get_arrival_features, "arrival_mode"),
        (get_chief_complaint_features, "cc_chest_pain"),
        (get_demographic_features, "age"),
    ],
)
def test_feature_group_helpers_find_expected_column(synthetic_raw_df, helper, expected_hit):
    result = helper(synthetic_raw_df.columns)
    assert expected_hit in result
