import seaborn as sns
sns.pairplot(df)
# scatter plot matrix of all numeric value in the table
sns.pairplot(df,hue='Age',diag_kind='hist')
# scatter plot matrix with labelled data (showed in different colour, labelled by the feature 'Age'), the charts on the diag line will be histogram

sns.boxplot(df['A'],orient='v')
# box plot for 1-dimensional data
sns.boxplot(x='Age',y='Price',data=df)
# box plot comparing group observations by a catrgorical feature (x)
sns.scatterplot(x='Age',y='Price',data=df)
# scatter plot
sns.heatmap(dist,square=True,xticklabels=False, yticklabels=False,cmap='Blues')
# heatmap, work for distance matrix


import matplotlib.pyplot as plt
plt.scatter(d['x'],d['y'],c=d['Type'],marker=markerTypes[d['Type']],s=60)
# Scatter with different color & marker for different types
plt.pie(d['x'],labels=d['y'])
# pie chart, compute the sum of d['x'] of each value of d['y']

plt.title('aaaa')
# set the title of a plot

import pandas as pd
df['Year'].hist(bins=5)
# histogram of the column
df['Year'].boxplot()
# boxplot of the column
df.boxplot(figsize=(20,3))
# boxplot of all numeric columns in the table (better have similar resolvation)
