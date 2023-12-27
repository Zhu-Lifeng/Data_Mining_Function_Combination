from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
# the model itself
print('Training dataset accuracy: {0}.'.format(knn.score(X, y)))
# knn.score is the function to compute the accuracy
y_pred=knn.predict(X)
mistake=np.nonzero(y_pred != y)[0]
# get the indices of misclassified samples
