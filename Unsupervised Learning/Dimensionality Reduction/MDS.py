from sklearn.manifold import MDS

embedding = MDS(n_components=2)
Xp = embedding.fit_transform(df.drop(['Tag']))
df_projection = pd.DataFrame({'x': Xp[:, 0], 'y': Xp[:, 1],'Tag': df['Tag']})
# multidimensional scaling, better use a standardized matrix as the input
# output a matrix contains a 2-dimensional point for each sample
