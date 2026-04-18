"""
DataLens Quickstart — run: python examples/quickstart.py
"""
import pandas as pd, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import datalens as dl

# 1. สร้างข้อมูลตัวอย่าง
df = pd.DataFrame({
    "region":  ["North","South","East","West","North","South"],
    "month":   ["Jan","Jan","Jan","Jan","Feb","Feb"],
    "revenue": [120, 200, None, 175, 135, 210],
    "cost":    [80, 130, 95, 110, 90, 140],
})

# 2. ดูรายงานข้อมูล
print("=== Profile ===")
report = dl.profile(df)
print(f"Shape: {report['shape']}, Missing: {report['missing']}")

# 3. ทำความสะอาด
df = dl.clean(df)
print(f"\nหลัง clean — missing: {df.isnull().sum().sum()}")

# 4. ดูคำแนะนำกราฟ
print("\n=== Chart Suggestions ===")
for s in dl.suggest_charts(df)[:3]:
    print(f"  [{s['chart_type']}] {s['reason']}")

# 5. สร้าง dashboard
dl.create_dashboard(output_path="dashboard.py")
print("\nรัน dashboard ด้วย: streamlit run dashboard.py")
