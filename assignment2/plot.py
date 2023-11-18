import pandas as pd
import plotly.express as px
from pathlib import Path

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

this_file_dir = Path('__file__').parent
bld = this_file_dir / "bld"
data_path = bld / "merged_data.csv"

score_names = {
    "antisocial": "bpiA",
    "anxiety": "bpiB",
    "headstrong": "bpiC",
    "hyperactive": "bpiD",
    "peer": "bpiE",
}

def create_plots():
    """Creates plots of the score for every attribute calculated against the scores in the chs dataset by age group 
    and writes them in html files
    """
    merged_data_df = pd.read_csv(data_path)

    for key in score_names:
        fig = px.scatter(data_frame = merged_data_df, x = key, y = score_names[key], facet_col="age", trendline="ols")

        file_name = "plots_"+key+".html"
        fig.write_html(bld / file_name)

if __name__ == "__main__":
    create_plots()