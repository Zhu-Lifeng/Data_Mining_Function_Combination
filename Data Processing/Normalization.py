import pandas as pd
Z = (df['a']-df['a'].mean())/df.['a'].std()
# Z-score


bins = pd.cut(df['b'],4)
# discretize the attribute into 4 bins (equal-width)
bins = pd.qcut(df['b'],4)
# discretize the attribute into 4 bins (equal-depth)
