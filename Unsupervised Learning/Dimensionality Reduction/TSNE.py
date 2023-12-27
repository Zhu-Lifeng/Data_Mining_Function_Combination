from sklearn.manifold import TSNE

embedding = TSNE(n_components=2, perplexity=100)
Xp = embedding.fit_transform(df.drop(['Tag']))
df_projection = pd.DataFrame({'x': Xp[:, 0], 'y': Xp[:, 1],'Tag': df['Tag']})
# t-distributed stochastic neighbour embedding (TSNE)
# better use a standardized matrix as the input
# output a matrix contains a 2-dimensional point for each sample
