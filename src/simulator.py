import time


def stream_sensor_data(df, delay=1):

    for _, row in df.iterrows():

        yield row

        time.sleep(delay)