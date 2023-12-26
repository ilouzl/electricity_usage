import pandas as pd


def parse_report(path):
    if path.endswith('.xlsx'):
        return read_pazgaz_report(path)
    elif path.endswith('.csv'):
        return read_iec_report(path)


def read_pazgaz_report(path):
    df = pd.read_excel(path, skiprows=2)
    df.rename(columns={'צריכה': 'consumption', 'תאריך קריאה': 'ts'}, inplace=True)
    df.set_index('ts', inplace=True, drop=True)
    dropped_columns = df.columns.tolist(); dropped_columns.remove('consumption')
    df.drop(columns=dropped_columns, axis=1, inplace=True)
    return df


def read_iec_report(path):
    df = pd.read_csv(path, skiprows=20, header=None, names=['date', 'time', 'consumption'])
    df['ts'] = pd.to_datetime(df.date + ' ' + df.time)
    df.set_index('ts', inplace=True, drop=True)
    dropped_columns = df.columns.tolist(); dropped_columns.remove('consumption')
    df.drop(columns=dropped_columns, axis=1, inplace=True)
    return df