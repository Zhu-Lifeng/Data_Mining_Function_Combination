import pandas as pd

df.groupby('Age').mean()
# make an aggregation based on the feature 'Age' (mean,sum,median,.......)

daily.index = pd.to_datetime(daily['DATE'])
# set the datetime as the index

monthly = daily.groupby(pd.Grouper(freq='M')).sum()
annually = daily.groupby(pd.Grouper(freq='Y')).sum()
# make a monthly/annually aggregation (in this case sum, also work for mean, median,......)
