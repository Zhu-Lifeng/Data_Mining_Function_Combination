from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier

knn_pipe = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=1))

knn_pipe.fit(X_train, y_train)
print('Test dataset accuracy: {0}.'.format(knn_pipe.score(X_test, y_test)))
