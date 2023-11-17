import pandas as pd
from pathlib import Path

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

this_file_dir = Path(__file__).parent
bld = this_file_dir / "bld"

def clean_and_reshape_nlsy_data(raw, info):
    pass

def clean_year_data(raw, year, info):
    df = pd.DataFrame(index=raw.index)
    df = _clean_bpi_variables(raw,info)
    for i in df.columns[:2]:
        df[i]= df[i].astype(pd.Int32Dtype()).astype(pd.CategoricalDtype())
    for i in df.columns[3:]:
        df[i] = _clean_bpi_cat(df[i])
    
    df = pd.wide_to_long(df, stubnames= info.readable_name.unique(),i= 'childid invariant', j='year', sep= " ")
    df = df.drop(columns=['childid','momid','birth_order'])
    df.index.names = ['childid', 'year']
    df = df.rename(columns= {'momid invariant': 'momid', 'birth_order invariant': 'birth_order'})
    df = df.sort_index()
    df = pd.concat([df, _add_subscale_scores(df)], axis=1)
    return df.xs(year, level=1)

def _clean_bpi_variables(raw_df, info_df):
     raw_df = raw_df[info_df["nlsy_name"]]  # choosing variables that are available in info 
     clean_variables = dict(zip(info_df.nlsy_name, info_df.readable_name +  ' ' + info_df.survey_year)) # creating a dictionary to rename columns in raw data
     return raw_df.rename(columns=clean_variables)

def _clean_bpi_cat(sr):
    sr = sr.replace([-7.0, -3.0, -2.0, -1.0], pd.NA)
    sr = sr.replace({'Never Attended School': pd.NA, 'Multiple selection': pd.NA })
    categories = ["not true", "sometimes true", "often true"]
    sr = sr.astype(pd.StringDtype()).str.lower().astype(pd.CategoricalDtype(categories=categories, ordered=True))
    return sr

def _add_subscale_scores(df):
    mapping_dict = {
    'not true': 0,
    'sometimes true': 1,
    'often true': 1
    }
    subscale = df.copy()
    for i in subscale.columns[2:]:
        subscale[i] = subscale[i].map(mapping_dict)
    
    categories = ["antisocial", "anxiety", "headstrong", "hyperactive", "dependence","peer"]

    for i in categories:
        subscale[i] = subscale[[col for col in subscale.columns if col.startswith(i)]].mean(axis=1)
    
    subscale = subscale[categories]

    return subscale

  
if __name__ == "__main__":
    raw = pd.read_stata(bld / "BEHAVIOR_PROBLEMS_INDEX.dta")
    info = pd.read_csv(bld / "bpi_variable_info.csv")
    
    df = clean_year_data(raw,1998,info)
    df
   #  df.to_csv(bld / "clean_year_date.csv")

