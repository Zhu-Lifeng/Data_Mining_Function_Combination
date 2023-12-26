import seaborn as sns
sns.pairplot(df)
# seaborn plot matirx of all numeric value in the table
import matplotlib.pyplot as plt

import pandas as pd
df['Year'].hist(bins=5)
# histogram of the column
df['Year'].boxplot()
# boxplot of the column
df.boxplot(figsize=(20,3))
# boxplot of all numeric columns in the table (better have similar resolvation)
