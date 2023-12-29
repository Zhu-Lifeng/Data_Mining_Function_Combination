rolling = series.rolling(window=3) # using a window of 3 samples: t, t-1, t-2
rolling_mean = rolling.mean()
#Trailing Moving Average
