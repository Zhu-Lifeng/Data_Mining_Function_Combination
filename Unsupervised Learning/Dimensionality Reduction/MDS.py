from sklearn.manifold import MDS

embedding = MDS(n_components=2)
Xp = embedding.fit_transform(df.drop('Tag'))
df_projection = pd.DataFrame({'x': Xp[:, 0], 'y': Xp[:, 1],'Tag': df['Tag']})
