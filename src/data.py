"""
src/data.py

Dataset loading, feature selection and modelling-frame construction for
the ED triage ESI prediction project.

Refactored from the Week 6 / Week 7 exploratory notebooks. Logic is
unchanged from those notebooks — this module only restructures it into
named, testable functions with explicit parameters. Nothing in this
module has side effects at import time (no top-level print statements,
no file reads at import time).
"""

from pathlib import Path
from typing import Iterable, Optional

import pandas as pd

DEFAULT_LEAKAGE_KEYWORDS = (
    "admit",
    "admission",
    "disposition",
    "hospital",
    "los",
    "outcome",
    "death",
    "mortality",
    "icu",
)


def load_dataset(path: str, index_col: int = 0) -> pd.DataFrame:
    """
    Load the raw triage dataset from a CSV file.

    Parameters
    ----------
    path : str
        Path to the dataset CSV file.
    index_col : int, default 0
        Column to use as the DataFrame index, matching the convention
        used in the Week 6 / Week 7 notebooks.

    Returns
    -------
    pd.DataFrame
        The raw, unmodified dataset.

    Raises
    ------
    FileNotFoundError
        If no file exists at `path`.
    """
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Could not locate dataset at '{path}'. "
            "Update the 'data.path' value in config.yaml, or place the "
            "file at this location."
        )
    return pd.read_csv(dataset_path, index_col=index_col)


def get_vital_features(columns: Iterable[str]) -> list:
    """Return columns that look like vital-sign measurements."""
    vital_terms = ("hr", "sbp", "dbp", "rr", "o2", "temp", "glucose")
    return [col for col in columns if any(term in col.lower() for term in vital_terms)]


def get_arrival_features(columns: Iterable[str]) -> list:
    """Return columns related to how/when the patient arrived."""
    return [col for col in columns if "arrival" in col.lower()]


def get_chief_complaint_features(columns: Iterable[str]) -> list:
    """Return one-hot chief-complaint flag columns (prefixed cc_)."""
    return [col for col in columns if col.lower().startswith("cc_")]


def get_demographic_features(columns: Iterable[str]) -> list:
    """
    Return the (deliberately narrow) demographic feature set used as
    predictors. Only age is included by design — gender, ethnicity,
    race, language, religion, marital status, employment status and
    insurance are excluded to avoid the model triaging patients
    differently based on who they are rather than their clinical
    presentation.
    """
    return [col for col in ("age",) if col in columns]


def select_features(df: pd.DataFrame) -> list:
    """
    Build the final predictor list for the model: demographic (age
    only), vital-sign, arrival and chief-complaint columns, in that
    order, with duplicates removed. Identical selection logic to the
    Week 6 / Week 7 notebooks.

    Parameters
    ----------
    df : pd.DataFrame
        The raw or lightly-filtered dataset to select predictors from.

    Returns
    -------
    list
        Ordered, de-duplicated list of predictor column names.
    """
    columns = df.columns
    selected = (
        get_demographic_features(columns)
        + get_vital_features(columns)
        + get_arrival_features(columns)
        + get_chief_complaint_features(columns)
    )
    return list(dict.fromkeys(selected))


def check_leakage(
    df: pd.DataFrame,
    leakage_keywords: Optional[Iterable[str]] = None,
) -> list:
    """
    Identify columns that look like post-triage outcomes (admission,
    disposition, length of stay, mortality, etc.), so they can be
    confirmed excluded from the predictor set.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset to scan for leakage-prone column names.
    leakage_keywords : Iterable[str], optional
        Keywords to match against column names (case-insensitive).
        Defaults to DEFAULT_LEAKAGE_KEYWORDS.

    Returns
    -------
    list
        Column names matching one or more leakage keywords.
    """
    keywords = leakage_keywords if leakage_keywords is not None else DEFAULT_LEAKAGE_KEYWORDS
    return [col for col in df.columns if any(word in col.lower() for word in keywords)]


def build_model_dataframe(
    df: pd.DataFrame,
    selected_features: Iterable[str],
    target: str,
) -> pd.DataFrame:
    """
    Restrict the dataset to the chosen predictors and target, drop
    rows with a missing or non-numeric target, and cast the target to
    integer.

    Parameters
    ----------
    df : pd.DataFrame
        The raw dataset.
    selected_features : Iterable[str]
        Predictor columns to retain (see `select_features`).
    target : str
        Name of the target column (the ESI level).

    Returns
    -------
    pd.DataFrame
        A modelling-ready frame containing only the selected features
        and a clean, integer target column.
    """
    feature_list = list(selected_features)
    model_df = df[feature_list + [target]].copy()

    model_df = model_df.dropna(subset=[target])
    model_df[target] = pd.to_numeric(model_df[target], errors="coerce")
    model_df = model_df.dropna(subset=[target])
    model_df[target] = model_df[target].astype(int)

    return model_df


def split_features_and_target(model_df: pd.DataFrame, target: str):
    """
    Split a modelling-ready frame into predictor matrix X and target
    vector y.

    Parameters
    ----------
    model_df : pd.DataFrame
        Output of `build_model_dataframe`.
    target : str
        Name of the target column.

    Returns
    -------
    tuple[pd.DataFrame, pd.Series]
        (X, y)
    """
    feature_columns = [col for col in model_df.columns if col != target]
    return model_df[feature_columns], model_df[target]
