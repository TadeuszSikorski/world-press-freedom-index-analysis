import pandas as pd
import preprocessing.clean_data as cd


files = [f"data/{year}.csv" for year in range(2002, 2022) if year != 2011]

df = pd.concat((pd.read_csv(f, sep=";", decimal=",") for f in files), ignore_index=True)

df = cd.format_year_value(df)

df = cd.drop_translation_columns(df)
