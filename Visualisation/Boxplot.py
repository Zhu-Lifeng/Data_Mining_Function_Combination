import seaborn as sns

sns.boxplot(df['A'],orient='v')
# box plot for 1-dimensional data
ax =sns.boxplot(x='Age',y='Price',data=df)
# box plot comparing group observations by a catrgorical feature (x)
import textwrap
ax.set_xticklabels([textwrap.fill(t.get_text(), 10)  for t in ax.get_xticklabels()])
# Wrap xticks 


import pandas as pd

df['Year'].boxplot()
# boxplot of the column
df.boxplot(figsize=(20,3))
# boxplot of all numeric columns in the table (better have similar resolvation)
