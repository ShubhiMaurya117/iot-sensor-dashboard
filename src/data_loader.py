import pandas as pd
def load_data(filepath):
    df = pd.read_csv(filepath)

    df.columns = ['id', 'room_id', 'noted_date', 'temp', 'out_in']

    df['noted_date'] = pd.to_datetime(
        df['noted_date'],
        format='mixed',
        dayfirst=True
    )

    df = df.dropna()

    return df