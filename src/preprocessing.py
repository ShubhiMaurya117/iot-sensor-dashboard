def split_indoor_outdoor(df):

    indoor = df[df['out_in'] == 'In']
    outdoor = df[df['out_in'] == 'Out']

    return indoor, outdoor