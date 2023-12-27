from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=10, random_state=0)
y_pred = kmeans.fit_predict(X)
# the model itself

from sklearn.metrics import silhouette_score
max_k = 15

# Sum of squared errors for each k
sses = []

# Silhouette coefficient for each k
silhouettes = []

for k in range(2, max_k + 1):
    kmeans = KMeans(n_clusters=k, random_state=0)
    y_pred = kmeans.fit_predict(X)
    
    sses.append(kmeans.inertia_)
    silhouettes.append(silhouette_score(X, y_pred))

# Plotting sums of squared errors
df = pd.DataFrame({'sum of squared errors': sses, 'number of clusters': list(range(2, max_k + 1))})
sns.lineplot(x='number of clusters', y='sum of squared errors', data=df)
plt.xticks(df['number of clusters'])
plt.show()

# Plotting silhouette coefficients
df = pd.DataFrame({'silhouette coefficient': silhouettes, 'number of clusters': list(range(2, max_k + 1))})
sns.lineplot(x='number of clusters', y='silhouette coefficient', data=df)
plt.xticks(df['number of clusters'])
plt.show()

# to compare the quality of clusterings of the same dataset for different numbers of clusters.
# use both sums of squared errors & silhouette coefficients
