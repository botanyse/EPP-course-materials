import pandas as pd
from pathlib import Path

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

this_file_dir = Path(__file__).parent
bld = this_file_dir / "bld"
data_path = bld / "chs_data.dta"

def clean_chs_data(raw): 
    """Clean 'raw' DataFrame, create a new DataFrame with the same index as 'raw' and fill in with cleaned columns of 'raw'.
    Function involves replacing negative values of columns from 'bpiA' to 'bpiE' are with pd.NA, changing datatypes of 'momid','age','childid','year', and setting 'childid' and 'year' as index.
    
    Args:
        raw (pd.DataFrame): Raw data to be cleaned.

    Returns:
        df (pd.DataFrame): The cleaned data.
    """
    df = pd.DataFrame(index = raw.index)
    df["momid"] = _change_data_types(raw["momid"])
    df["age"] = _change_data_types(raw["age"])
    for i in ["bpiA", "bpiB", "bpiC", "bpiD", "bpiE"]:
        df[i] = _clean_bpi(raw[i])
    df = df.set_index([_change_data_types(raw["childid"]), _change_data_types(raw["year"])])
    return df

def _clean_bpi(sr):
    """Replace BPI values '-100' with pd.NA."""
    sr = sr.astype(pd.Float32Dtype())
    sr = sr.replace({-100.000000: pd.NA})
    return sr

def _change_data_types(sr):
    """Change datatype to UInt32."""
    return sr.astype(pd.UInt32Dtype())

if __name__ == "__main__":
    raw = pd.read_stata(data_path)
    df = clean_chs_data(raw)
    df.to_feather(bld / "clean_chs_data.arrow")

