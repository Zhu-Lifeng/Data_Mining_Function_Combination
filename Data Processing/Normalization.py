import pandas as pd
Z = (df['a']-df['a'].mean())/df.['a'].std()
# Z-score


bins = pd.cut(df['b'],4)
# discretize the attribute into 4 bins (equal-width)
bins = pd.qcut(df['b'],4)
# discretize the attribute into 4 bins (equal-depth)

dfO['Home_or_restaurant']=df['Home_or_restaurant'].apply(lambda x: 'C' if x != 'A' and x != 'B' else x)
# replace all value other than 'A' or 'B' with 'C'
dfO['Home_or_restaurant']=dfO['Home_or_restaurant'].map({'home': 0, 'restaurant': 1})
# replace muti-type of values with a map
