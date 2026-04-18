from __future__ import annotations
import pandas as pd
from typing import Optional, List

THEME = {
    "font_family": "Arial, sans-serif",
    "title_font_size": 22,
    "axis_font_size": 13,
    "colorscale": [
        "#2E86AB", "#A23B72", "#F18F01", "#C73E1D",
        "#3B1F2B", "#44BBA4", "#E94F37", "#393E41"
    ],
}

CHART_RULES = {
    "histogram": "Numeric column — distribution of a single variable",
    "bar": "Categorical vs Numeric — compare values across categories",
    "line": "DateTime index — trend over time",
    "scatter": "Two numeric columns — relationship between variables",
    "heatmap": "Correlation matrix — relationships between all numeric columns",
    "box": "Numeric + Categorical — distribution per group",
}


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


def plot(
    df: pd.DataFrame,
    chart_type: Optional[str] = None,
    x: Optional[str] = None,
    y: Optional[str] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    save_png: Optional[str] = None,
    **kwargs,
):
    """
    Plot a professional chart using Plotly.

    Args:
        df: Input DataFrame.
        chart_type: 'bar', 'line', 'scatter', 'histogram', 'heatmap', 'box'.
        x: Column for x-axis.
        y: Column for y-axis.
        title: Chart title.
        color: Column to use for color grouping.
        save_png: File path to save chart as PNG (e.g. 'chart.png').

    Examples:
        >>> fig = dl.plot(df, chart_type="bar", x="region", y="revenue", title="Revenue by Region")
        >>> fig = dl.plot(df, chart_type="bar", x="region", y="revenue", save_png="chart.png")
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

    auto_title = title or (f"{y} by {x}" if x and y else chart_type.title())

    if chart_type == "heatmap":
        import plotly.graph_objects as go
        corr = df.select_dtypes(include="number").corr().round(2)
        fig = go.Figure(data=go.Heatmap(
            z=corr.values,
            x=corr.columns.tolist(),
            y=corr.index.tolist(),
            colorscale="RdBu",
            zmid=0,
            text=corr.values.round(2),
            texttemplate="%{text}",
        ))
    else:
        chart_map = {
            "bar": px.bar,
            "line": px.line,
            "scatter": px.scatter,
            "histogram": px.histogram,
            "box": px.box,
        }
        if chart_type not in chart_map:
            raise ValueError(f"Unknown chart_type '{chart_type}'.")
        kw = {k: v for k, v in {
            "x": x, "y": y, "color": color, "title": auto_title,
            "color_discrete_sequence": THEME["colorscale"],
        }.items() if v is not None}
        kw.update(kwargs)
        fig = chart_map[chart_type](df, **kw)

    fig.update_layout(
        title=dict(
            text=auto_title,
            font=dict(size=THEME["title_font_size"], family=THEME["font_family"], color="#1a1a2e"),
            x=0.05,
        ),
        font=dict(family=THEME["font_family"], size=THEME["axis_font_size"], color="#444"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=False, linecolor="#ccc", linewidth=1),
        yaxis=dict(gridcolor="#f0f0f0", linecolor="#ccc", linewidth=1),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="#ccc", borderwidth=1),
        margin=dict(l=60, r=40, t=80, b=60),
    )

    if save_png:
        try:
            fig.write_image(save_png)
            print(f"Chart saved: {save_png}")
        except Exception:
            print("To save PNG, run: pip install kaleido")

    return fig
