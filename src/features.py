"""
src/features.py

Feature engineering for the ED triage ESI prediction project.

This module contains two things:
  1. The same feature-grouping helpers used by src/data.py (re-exported
     here so feature engineering and feature selection can evolve
     independently as the project grows).
  2. New engineered features, added in response to Week 7 tutor
     feedback suggesting engineered features might improve performance
     beyond the raw vital signs.

Nothing in this module has side effects at import time.
"""

from typing import Optional

import numpy as np
import pandas as pd


def add_engineered_features(
    df: pd.DataFrame,
    hr_col: str = "hr",
    sbp_col: str = "sbp",
    dbp_col: str = "dbp",
) -> pd.DataFrame:
    """
    Add clinically-motivated engineered features derived from vital
    signs already present in the dataset.

    Two features are added, both standard early-warning indicators
    used in real triage/track-and-trigger systems, so they carry
    genuine clinical meaning rather than being arbitrary derived
    columns:

    - ``shock_index``: heart rate divided by systolic blood pressure.
      A rising shock index is an early indicator of haemodynamic
      compromise (e.g. occult haemorrhage or sepsis) and can flag
      deterioration before either vital sign alone crosses an
      individual threshold.
    - ``pulse_pressure``: systolic minus diastolic blood pressure.
      An abnormally narrow or wide pulse pressure is independently
      associated with cardiovascular instability.

    Rows missing either input vital sign, or with a systolic blood
    pressure of zero (which would make shock_index undefined), get a
    NaN for the derived feature rather than raising an error, so this
    function is safe to call on real, imperfect clinical data.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset containing the source vital-sign columns.
    hr_col, sbp_col, dbp_col : str
        Column names for heart rate, systolic and diastolic blood
        pressure respectively. Defaults match the raw dataset's
        column names; override if your column names differ.

    Returns
    -------
    pd.DataFrame
        A copy of `df` with `shock_index` and `pulse_pressure` added
        as new columns. Source columns are left unchanged. If any
        required source column is missing, that engineered feature is
        skipped (not added) rather than raising an error.
    """
    result = df.copy()

    if hr_col in result.columns and sbp_col in result.columns:
        safe_sbp = result[sbp_col].replace(0, np.nan)
        result["shock_index"] = result[hr_col] / safe_sbp

    if sbp_col in result.columns and dbp_col in result.columns:
        result["pulse_pressure"] = result[sbp_col] - result[dbp_col]

    return result


def get_engineered_feature_names(
    df: pd.DataFrame,
    hr_col: str = "hr",
    sbp_col: str = "sbp",
    dbp_col: str = "dbp",
) -> list:
    """
    Return the names of engineered features that `add_engineered_features`
    would actually add for this DataFrame, given which source columns
    are present. Useful for building the final predictor list without
    duplicating the presence checks in `add_engineered_features`.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset to check for the presence of source vital-sign columns.
    hr_col, sbp_col, dbp_col : str
        Source column names, matching `add_engineered_features`.

    Returns
    -------
    list
        Names of engineered features that would be added.
    """
    names = []
    if hr_col in df.columns and sbp_col in df.columns:
        names.append("shock_index")
    if sbp_col in df.columns and dbp_col in df.columns:
        names.append("pulse_pressure")
    return names
