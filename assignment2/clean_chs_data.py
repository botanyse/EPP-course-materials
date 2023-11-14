import pandas as pd
from pathlib import Path

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

this_file_dir = Path(__file__).parent
bld = this_file_dir / "bld"
data_path = bld / "chs_data.dta"

def clean_chs_data(raw):
    df = pd.DataFrame(index = raw.index)
    for i in ["bpiA", "bpiB", "bpiC", "bpiD", "bpiE"]:
        df[i] = _clean_bpi(raw[i])
    df["momid"] = _clean_momid_and_childid(raw["momid"])
    df["age"] = raw["age"]
    df = df.set_index([_clean_momid_and_childid(raw["childid"]), raw["year"]])
    return df

def _clean_bpi(sr):
    sr = sr.replace({-100.000000: pd.NA})
    return sr

def _clean_momid_and_childid(sr):
    return sr.astype(pd.Int32Dtype()).astype(pd.CategoricalDtype())

if __name__ == "__main__":
    raw = pd.read_stata(data_path)
    df = clean_chs_data(raw)
    df.to_csv(bld / "clean_chs_data.csv")

