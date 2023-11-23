import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

def create_plots(df):
    fig = px.scatter(merged_data, x= y= value, facet_col="age", trendline="ols")
    return go.Figure(fig)

if __name__ == "__main__":
    this_file_dir = Path('__file__').parent
    bld = this_file_dir / "bld"
    merged_data = pd.read_feather(bld / "merged_data.arrow")

    score_names = {
    "antisocial": "bpiA",
    "anxiety": "bpiB",
    "headstrong": "bpiC",
    "hyperactive": "bpiD",
    "peer": "bpiE",
    }
    for key, value in score_names.items():
        create_plots(merged_data).write_image(key.png)