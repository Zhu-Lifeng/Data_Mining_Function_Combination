import seaborn as sns

sns.heatmap(dist,square=True,xticklabels=False, yticklabels=False,cmap='Blues')
# heatmap, work for distance matrix

import matplotlib.pyplot as plt
plt.imshow(dist,cmap='Blues',aspect='equal',interpolation='nearest')
plt.colorbar()
plt.xticks([])
plt.yticks([])
# heatmap, work for distance matrix, use nearest neighbour interpolation (mutiple squares)

plt.imshow(dist,cmap='Blues',aspect='equal',interpolation='bilinear')
plt.colorbar()
plt.xticks([])
plt.yticks([])
# heatmap, work for distance matrix, use bilinear interpolation (change smoothly)
