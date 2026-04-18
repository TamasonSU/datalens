<div align="center">

# 🔭 DataLens

**Load, clean, and visualize data in just a few lines.**

[![CI](https://github.com/TamasonSU/datalens/actions/workflows/ci.yml/badge.svg)](https://github.com/TamasonSU/datalens/actions)
[![Python](https://img.shields.io/pypi/pyversions/datalens.svg)](https://pypi.org/project/datalens/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

DataLens is a lightweight Python library that turns exploratory data analysis into a single line of code.

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
