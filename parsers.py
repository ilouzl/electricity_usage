import pandas as pd


def read_pazgaz_report(path):
    df = pd.read_excel(path, skiprows=2)
    df.rename(columns={'צריכה': 'consumption', 'תאריך קריאה': 'ts'}, inplace=True)
    df.set_index('ts', inplace=True, drop=True)
    dropped_columns = df.columns.tolist(); dropped_columns.remove('consumption')
    df.drop(columns=dropped_columns, axis=1, inplace=True)
    return df