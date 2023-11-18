import pandas as pd
from pathlib import Path

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

this_file_dir = Path(__file__).parent
bld = this_file_dir / "bld"

def merge_df(clean_chs,clean_nlys):
    clean_merged = pd.merge(clean_chs,clean_nlys,left_index=True, right_index=True, how='left', suffixes= (None, 'drop'))
    clean_merged = clean_merged.drop(columns='momiddrop')
    clean_merged = clean_merged[(clean_merged['age']<=13) & (clean_merged['age']>=5)]
    return clean_merged

if __name__ == "__main__":
    clean_chs = pd.read_feather(bld / "clean_chs_data.arrow")
    clean_nlsy = pd.read_feather(bld / "clean_nlsy_data.arrow")
    merged_data = merge_df(clean_chs, clean_nlsy)
    merged_data.to_csv(bld / "merged_data.csv")
    