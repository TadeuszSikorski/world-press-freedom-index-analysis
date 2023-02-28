import pandas as pd


def drop_translation_columns(df):
    return df.drop(columns=['FR_country', 'ES_country', 'AR_country', 'FA_country'])


def format_year_value(df):
    new_rows = []
    
    for index, row in df.iterrows():
        if isinstance(df.loc[index, 'Year (N)'], str):
            years = row['Year (N)'].replace('-', '-20').split('-')
            row['Year (N)'] = int(years[0])
            new_rows.append(row.to_dict())
            
            if len(years) == 2:
                new_row = row.to_dict()
                new_row['Year (N)'] = int(years[1])
                new_rows.append(new_row)
        else:
            new_rows.append(row.to_dict())
    
    return pd.DataFrame(new_rows)
