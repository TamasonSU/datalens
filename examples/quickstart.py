"""
DataLens Quickstart — run: python examples/quickstart.py
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import datalens as dl

# 1. Load data from CSV file
print("=== 1. Loading data ===")
df = dl.load("examples/sales_data.csv")
print(f"Loaded: {df.shape[0]} rows x {df.shape[1]} columns")
print(df.head())

# 2. Profile — check data quality
print("\n=== 2. Data Profile ===")
report = dl.profile(df)
print(f"Missing values: {report['missing']}")
print(f"Duplicates: {report['duplicates']}")

# 3. Clean — fix missing values and duplicates
print("\n=== 3. Cleaning data ===")
df = dl.clean(df)
print(f"Missing after clean: {df.isnull().sum().sum()}")

# 4. Get chart suggestions
print("\n=== 4. Chart Suggestions ===")
for s in dl.suggest_charts(df)[:3]:
    print(f"  [{s['chart_type']}] {s['reason']}")

# 5. Plot chart
print("\n=== 5. Plotting chart ===")
fig = dl.plot(df, chart_type="bar", x="region", y="revenue")
fig.show()
print("Chart opened in browser!")
