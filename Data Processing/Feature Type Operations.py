import pandas as pd

df = df.astype({'Name':'string','Price':'float64','Year':'category','Age':'int64'})
# change the type of columns in the table
df['Price']=pd.to_numeric(df['Price'])
# turn a column into a numeric one
df['Date']=pd.to_datatime(df['Date'])
# turn a column into a numeric one
