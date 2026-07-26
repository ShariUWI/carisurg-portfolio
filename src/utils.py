"""
src/utils.py

Small shared helpers used across the ED triage ESI prediction project:
reproducible seeding and config loading.

Nothing in this module has side effects at import time.
"""

from pathlib import Path
from typing import Any, Dict

import numpy as np
import yaml


def set_random_seed(seed: int) -> int:
    """
    Seed numpy's global random state for reproducibility.

    Parameters
    ----------
    seed : int
        The seed value (project default: 42, see config.yaml).

    Returns
    -------
    int
        The seed that was set, for convenient logging by the caller.
    """
    np.random.seed(seed)
    return seed


def load_config(path: str) -> Dict[str, Any]:
    """
    Load a YAML config file into a plain dict.

    Parameters
    ----------
    path : str
        Path to the config file (e.g. "config.yaml").

    Returns
    -------
    dict
        Parsed config contents.

    Raises
    ------
    FileNotFoundError
        If no file exists at `path`.
    """
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Could not locate config file at '{path}'.")

    with open(config_path, "r") as f:
        return yaml.safe_load(f)
