from __future__ import annotations
import pandas as pd
from typing import Optional


def profile(df: pd.DataFrame) -> dict:
    """Generate a data quality report."""
    report = {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing": df.isnull().sum().to_dict(),
        "missing_pct": (df.isnull().mean() * 100).round(2).to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "numeric_summary": {},
    }
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        report["numeric_summary"] = df[numeric_cols].describe().round(2).to_dict()
    return report


def clean(
    df: pd.DataFrame,
    drop_duplicates: bool = True,
    fill_strategy: Optional[str] = "median",
    drop_threshold: float = 0.9,
) -> pd.DataFrame:
    """
    Auto-clean a DataFrame.

    Args:
        drop_duplicates: Remove duplicate rows.
        fill_strategy: 'median', 'mean', 'mode', or None.
        drop_threshold: Drop columns missing more than this fraction.
    """
    df = df.copy()
    missing_pct = df.isnull().mean()
    cols_to_drop = missing_pct[missing_pct > drop_threshold].index.tolist()
    if cols_to_drop:
        df = df.drop(columns=cols_to_drop)
    if drop_duplicates:
        df = df.drop_duplicates()
    if fill_strategy:
        numeric_cols = df.select_dtypes(include="number").columns
        categorical_cols = df.select_dtypes(include=["object", "category"]).columns
        if fill_strategy == "median":
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        elif fill_strategy == "mean":
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        elif fill_strategy == "mode":
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mode().iloc[0])
        df[categorical_cols] = df[categorical_cols].fillna("Unknown")
    return df
