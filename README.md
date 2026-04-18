<div align="center">

# 🔭 DataLens

**Load, clean, and visualize data in just a few lines.**

[![CI](https://github.com/TamasonSU/datalens/actions/workflows/ci.yml/badge.svg)](https://github.com/TamasonSU/datalens/actions)
[![Python](https://img.shields.io/pypi/pyversions/datalens.svg)](https://pypi.org/project/datalens/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

DataLens is a lightweight Python library that turns exploratory data analysis into a single line of code.
<img width="2005" height="653" alt="image" src="https://github.com/user-attachments/assets/4d07aa37-18c9-4da7-ac76-c19056a3c991" />


```python
import datalens as dl

df  = dl.load("sales.csv")
df  = dl.clean(df)
rep = dl.profile(df)
fig = dl.plot(df, x="region", y="revenue")
fig.show()
```

## Installation

**Step 1 — Download the project**

Go to [https://github.com/TamasonSU/datalens](https://github.com/TamasonSU/datalens), click **Code → Download ZIP**, then extract the folder.

**Step 2 — Open terminal and go to the folder**

```bash
cd Desktop/datalens_project
```

**Step 3 — Install required libraries**

```bash
pip install pandas plotly openpyxl narwhals --no-deps --ignore-requires-python
```

**Step 4 — Test it works**

```bash
python examples/quickstart.py
```

## Quick example

Open Python and try:

```python
import sys
sys.path.insert(0, ".")
import datalens as dl
import pandas as pd

df = pd.DataFrame({
    "region": ["North", "South", "East", "West"],
    "revenue": [120, 200, 150, 300],
})

fig = dl.plot(df, chart_type="bar", x="region", y="revenue")
fig.show()
```

**How to load your own file**

**Option 1 — Put your file in the project folder (easiest)**

Copy your Excel or CSV file into the `datalens_project` folder, then load it like this:

```python
df = dl.load("mydata.xlsx")
df = dl.load("sales.csv")
```

**Option 2 — Use the full path to your file**

No need to move your file, just paste the full path:

```python
# Windows
df = dl.load("C:/Users/yourname/Documents/mydata.xlsx")

# Mac / Linux
df = dl.load("/Users/yourname/Documents/mydata.xlsx")
```

## Usage

**Step 1 — Open Python**

```bash
python
```

**Step 2 — Load your data**

```python
import sys
sys.path.insert(0, ".")
import datalens as dl

# Put your file in the project folder and load by filename
df = dl.load("sales_data.csv")

# Or use full path — no need to move your file
df = dl.load("C:/Users/yourname/Documents/mydata.xlsx")
```

**Step 3 — Check data quality**

```python
print(dl.profile(df))
```

**Step 4 — Clean your data**

```python
df = dl.clean(df)
```

**Step 5 — Get chart suggestions**

```python
dl.suggest_charts(df)
```

**Step 6 — Plot a chart**

```python
fig = dl.plot(df, chart_type="bar", x="region", y="revenue", title="Revenue by Region")
fig.show()
```

**Step 7 — Save chart as PNG**

```python
fig = dl.plot(df, chart_type="bar", x="region", y="revenue", save_png="chart.png")
```

## Run tests

```bash
pip install pytest
pytest
```

## Troubleshooting

**THESE PACKAGES DO NOT MATCH THE HASHES error**

```bash
pip install pandas plotly openpyxl narwhals --no-deps --ignore-requires-python
```

**ModuleNotFoundError: No module named 'narwhals'**

```bash
pip install narwhals
```

**Still cannot install — try upgrading pip first**

```bash
python -m pip install --upgrade pip
pip install pandas plotly openpyxl narwhals
```

## License

MIT — see [LICENSE](LICENSE)
