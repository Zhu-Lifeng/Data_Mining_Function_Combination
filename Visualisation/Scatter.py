import seaborn as sns
sns.scatterplot(x='Age',y='Price',data=df)
# scatter plot

sns.pairplot(df)
# scatter plot matrix of all numeric value in the table
sns.pairplot(df,hue='Age',diag_kind='hist')
# scatter plot matrix with labelled data (showed in different colour, labelled by the feature 'Age'), the charts on the diag line will be histogram

import matplotlib.pyplot as plt
plt.scatter(d['x'],d['y'],c=d['Type'],marker=markerTypes[d['Type']],s=60)
# Scatter with different color & marker for different types
