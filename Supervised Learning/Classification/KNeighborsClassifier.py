from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
print('Training dataset accuracy: {0}.'.format(knn.score(X, y)))
