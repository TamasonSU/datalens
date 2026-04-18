import pytest, pandas as pd, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from datalens.visualizers.core import suggest_charts

@pytest.fixture
def df():
    return pd.DataFrame({"region":["N","S","E","W"], "revenue":[100,200,150,300], "cost":[80,120,90,200]})

def test_returns_list(df):
    assert isinstance(suggest_charts(df), list)

def test_has_keys(df):
    for s in suggest_charts(df):
        assert "chart_type" in s and "columns" in s and "reason" in s

def test_bar_for_categorical(df):
    assert "bar" in [s["chart_type"] for s in suggest_charts(df)]
