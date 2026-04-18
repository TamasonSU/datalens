import pytest, pandas as pd, numpy as np, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from datalens.cleaners.core import clean, profile

@pytest.fixture
def df():
    return pd.DataFrame({"name": ["Alice","Bob","Alice",None],
                          "score": [88.0,None,88.0,75.0],
                          "age": [30,25,30,None]})

def test_profile(df):
    r = profile(df)
    assert r["shape"] == (4, 3)
    assert r["missing"]["name"] == 1

def test_clean_duplicates(df):
    assert clean(df).duplicated().sum() == 0

def test_clean_fills(df):
    assert clean(df)["score"].isnull().sum() == 0
