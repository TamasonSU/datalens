from __future__ import annotations
import pandas as pd
from pathlib import Path
from typing import Optional

TEMPLATE = '''"""Auto-generated DataLens Dashboard — run: streamlit run {filename}"""
import streamlit as st
import datalens as dl

st.set_page_config(page_title="DataLens Dashboard", layout="wide")
st.title("DataLens Dashboard")

uploaded = st.sidebar.file_uploader("Upload your data", type=["csv", "json", "xlsx"])
if uploaded:
    df = dl.load(uploaded)
else:
    st.info("Upload a file from the sidebar to get started.")
    st.stop()

with st.expander("Data Profile", expanded=False):
    report = dl.profile(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", report["shape"][0])
    col2.metric("Columns", report["shape"][1])
    col3.metric("Duplicates", report["duplicates"])
    st.dataframe(df.head(10))

st.sidebar.subheader("Cleaning Options")
fill_strategy = st.sidebar.selectbox("Fill missing values", ["median", "mean", "mode", "none"])
if st.sidebar.button("Clean Data"):
    df = dl.clean(df, fill_strategy=fill_strategy if fill_strategy != "none" else None)
    st.success("Data cleaned!")

st.subheader("Smart Charts")
for s in dl.suggest_charts(df)[:4]:
    st.caption(s["reason"])
    cols = s["columns"]
    fig = dl.plot(df, chart_type=s["chart_type"],
                  x=cols[0] if len(cols) > 0 else None,
                  y=cols[1] if len(cols) > 1 else None)
    st.plotly_chart(fig, use_container_width=True)
'''


def create_dashboard(df: Optional[pd.DataFrame] = None, output_path: str = "dashboard.py") -> str:
    """Generate a ready-to-run Streamlit dashboard script."""
    code = TEMPLATE.format(filename=Path(output_path).name)
    with open(output_path, "w") as f:
        f.write(code)
    print(f"Created: {output_path}")
    print(f"Run with: streamlit run {output_path}")
    return output_path
