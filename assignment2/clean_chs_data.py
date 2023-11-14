import pandas as pd
from pathlib import Path

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

this_file_dir = Path(__file__).parent
bld = this_file_dir / "bld"
data_path = bld / "chs_data.dta"

def clean_chs_data(raw):
    df_index = [_clean_momid_and_childid(raw["childid"]), raw["year"]]
    df = pd.DataFrame(index = df_index)
    for i in ["bpiA", "bpiB", "bpiC", "bpiD", "bpiE"]:
        df[i] = _clean_bpi(raw[i])
    df["momid"] = _clean_momid_and_childid(raw["momid"])
    df["age"] = raw["age"]
    return df

def _clean_bpi(sr):
    sr = sr.replace({sr[i]: pd.NA for i in sr.index if sr[i]<0})
    return sr

def _clean_momid_and_childid(sr):
    return sr.astype(pd.Int32Dtype()).astype(pd.CategoricalDtype())

if __name__ == "__main__":
    raw = pd.read_stata(data_path)
    df = clean_chs_data(raw)
    df.to_feather(bld / "clean_chs_data.feather")
