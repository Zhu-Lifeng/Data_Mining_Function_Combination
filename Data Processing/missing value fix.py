import pandas as pd
import numpy as np
df['Name'].isna()
# assign all missing value row of the column with 1, others with 0 (work with np.NaN)
df['Name'].isna().sum()
# get the number of missing value in this column

data = data.fillna(data.mean())
data = data.fillna(data.median())
data = data.fillna(data.mode())
# fill the missing value with the mean/median/mode of the column (or any fixed value)
# work with np.NaN
# work for table data (replace a column with a fixed column)

data =data.dropna()
# delete all the missing value rows
# work with np.NaN
# work for 1-dimensional data
