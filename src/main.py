import pandas as pd
import preprocessing.clean_data as cd
import visualization.plot_data as v


files = [f"data/{year}.csv" for year in range(2002, 2022) if year != 2011]

df = pd.concat((pd.read_csv(f, sep=";", decimal=",") for f in files), ignore_index=True)

df = cd.format_year_value(df)

df = cd.drop_translation_columns(df)

v.plot_histogram_and_density(df, "Score N", "plots/histogram_and_density.jpg")
