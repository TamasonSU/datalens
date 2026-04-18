import pytest, pandas as pd, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from datalens.loaders.core import load

def test_load_csv(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("name,age\nAlice,30\nBob,25\n")
    df = load(str(f))
    assert df.shape == (2, 2)

def test_load_json(tmp_path):
    f = tmp_path / "test.json"
    f.write_text('[{"name":"Alice","age":30},{"name":"Bob","age":25}]')
    df = load(str(f))
    assert df.shape == (2, 2)

def test_load_unsupported_raises():
    with pytest.raises(ValueError):
        load("file.xyz")
