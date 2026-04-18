<div align="center">

# 🔭 DataLens

**Load, clean, and visualize data in just a few lines.**

[![CI](https://github.com/yourusername/datalens/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/datalens/actions)
[![Python](https://img.shields.io/pypi/pyversions/datalens.svg)](https://pypi.org/project/datalens/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

DataLens is a lightweight Python library that turns exploratory data analysis into a single line of code.

```python
import datalens as dl

df  = dl.load("sales.csv")          # load CSV, JSON, Excel, or URL
df  = dl.clean(df)                   # auto-fix missing values & duplicates
rep = dl.profile(df)                 # get a quality report instantly
fig = dl.plot(df, x="region", y="revenue")  # smart chart in one line
dl.create_dashboard(output_path="app.py")   # generate a Streamlit app
```

## Installation

```bash
pip install datalens
```

With Streamlit dashboard support:
```bash
pip install "datalens[dashboard]"
```

## Quickstart

```bash
python examples/quickstart.py
```

## Run tests

```bash
pip install -e ".[dev]"
pytest
```

## Troubleshooting

**Cannot install pandas / plotly on Windows**

If you see `THESE PACKAGES DO NOT MATCH THE HASHES` error, run this instead:

```bash
pip install pandas plotly openpyxl --no-deps --ignore-requires-python
```

**Still cannot install**

Try upgrading pip first, then install again:

```bash
python -m pip install --upgrade pip
pip install pandas plotly openpyxl
```

**ModuleNotFoundError: No module named 'narwhals'**

Run this to fix:

```bash
pip install narwhals
```

## License

MIT — see [LICENSE](LICENSE)
