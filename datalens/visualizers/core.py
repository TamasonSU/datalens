from __future__ import annotations
import pandas as pd
from typing import Optional, List


def suggest_charts(df: pd.DataFrame) -> List[dict]:
    """Suggest the best chart types for a DataFrame."""
    suggestions = []
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    datetime_cols = df.select_dtypes(include="datetime").columns.tolist()

    for col in datetime_cols:
        for num in numeric_cols:
            suggestions.append({"chart_type": "line", "columns": [col, num],
                "reason": f"'{col}' is datetime — great for showing '{num}' over time."})

    for cat in categorical_cols:
        for num in numeric_cols:
            suggestions.append({"chart_type": "bar", "columns": [cat, num],
                "reason": f"Compare '{num}' across '{cat}' categories."})

    if len(numeric_cols) >= 2:
        suggestions.append({"chart_type": "scatter", "columns": numeric_cols[:2],
            "reason": f"Explore relationship between '{numeric_cols[0]}' and '{numeric_cols[1]}'."})

    for col in numeric_cols[:3]:
        suggestions.append({"chart_type": "histogram", "columns": [col],
            "reason": f"See the distribution of '{col}'."})

    if len(numeric_cols) >= 3:
        suggestions.append({"chart_type": "heatmap", "columns": numeric_cols,
            "reason": "Show correlations between all numeric columns."})

    return suggestions


def plot(df: pd.DataFrame, chart_type: Optional[str] = None,
         x: Optional[str] = None, y: Optional[str] = None,
         title: Optional[str] = None, color: Optional[str] = None, **kwargs):
    """
    Plot a chart using Plotly. Auto-detects chart type if not specified.

    Examples:
        >>> fig = dl.plot(df, chart_type="bar", x="region", y="revenue")
        >>> fig.show()
    """
    try:
        import plotly.express as px
    except ImportError:
        raise ImportError("Run: pip install plotly")

    if chart_type is None:
        suggestions = suggest_charts(df)
        if suggestions:
            chart_type = suggestions[0]["chart_type"]
            cols = suggestions[0]["columns"]
            if x is None and len(cols) > 0:
                x = cols[0]
            if y is None and len(cols) > 1:
                y = cols[1]
        else:
            chart_type = "histogram"

    if chart_type == "heatmap":
        import plotly.graph_objects as go
        corr = df.select_dtypes(include="number").corr().round(2)
        fig = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns.tolist(),
            y=corr.index.tolist(), colorscale="RdBu", zmid=0))
    else:
        chart_map = {"bar": px.bar, "line": px.line, "scatter": px.scatter,
                     "histogram": px.histogram, "box": px.box}
        if chart_type not in chart_map:
            raise ValueError(f"Unknown chart_type '{chart_type}'.")
        kw = {k: v for k, v in {"x": x, "y": y, "color": color, "title": title}.items() if v is not None}
        kw.update(kwargs)
        fig = chart_map[chart_type](df, **kw)

    fig.update_layout(template="plotly_white")
    return fig
