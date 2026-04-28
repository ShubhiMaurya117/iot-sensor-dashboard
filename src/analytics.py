import pandas as pd


def daily_temperature_trends(df):

    daily = (
        df.groupby([df['noted_date'].dt.date, 'out_in'])['temp']
        .mean()
        .unstack()
    )

    # convert index to datetime
    daily.index = pd.to_datetime(daily.index)

    # fill missing values
    daily = daily.ffill()

    return daily

def monthly_temperature_trends(df):

    df['month'] = df['noted_date'].dt.strftime('%b %Y')

    month_order = (
        df.groupby('month')['noted_date']
        .min()
        .sort_values()
        .index
        .tolist()
    )

    monthly = (
        df.groupby(['month', 'out_in'])['temp']
        .mean()
        .unstack()
        .reindex(month_order)
    )

    return monthly

def generate_kpis(df, indoor, outdoor):

    current_indoor_temp = indoor.iloc[-1]['temp']

    current_outdoor_temp = outdoor.iloc[-1]['temp']

    highest_temp = df['temp'].max()

    average_temp = round(df['temp'].mean(), 2)

    return {
        "current_indoor_temp": current_indoor_temp,
        "current_outdoor_temp": current_outdoor_temp,
        "highest_temp": highest_temp,
        "average_temp": average_temp
    }

def generate_alert(df, threshold=40):

    latest_temp = df.iloc[-1]['temp']

    if latest_temp > threshold:

        return "HIGH TEMPERATURE ALERT"

    return "NORMAL"
def rolling_temperature_trend(df, window=50):

    rolling = (
        df.groupby('noted_date')['temp']
        .mean()
        .rolling(window=window)
        .mean()
    )

    return rolling