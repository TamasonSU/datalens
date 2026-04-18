from __future__ import annotations
import pandas as pd
from pathlib import Path
from typing import Union


def load(source: Union[str, Path], **kwargs) -> pd.DataFrame:
    """
    Load data from CSV, JSON, Excel, Parquet, or URL.

    Examples:
        >>> import datalens as dl
        >>> df = dl.load("data/sales.csv")
        >>> df = dl.load("https://example.com/data.json")
    """
    source = str(source)
    if source.startswith("http://") or source.startswith("https://"):
        return _load_url(source, **kwargs)
    elif source.endswith(".csv"):
        return pd.read_csv(source, **kwargs)
    elif source.endswith(".json"):
        return pd.read_json(source, **kwargs)
    elif source.endswith((".xlsx", ".xls")):
        return pd.read_excel(source, **kwargs)
    elif source.endswith(".parquet"):
        return pd.read_parquet(source, **kwargs)
    else:
        raise ValueError(f"Unsupported format: '{source}'. Use .csv .json .xlsx .parquet or http/https")


def _load_url(url: str, **kwargs) -> pd.DataFrame:
    if ".csv" in url:
        return pd.read_csv(url, **kwargs)
    elif ".json" in url:
        return pd.read_json(url, **kwargs)
    return pd.read_csv(url, **kwargs)
