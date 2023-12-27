from sklearn.model_selection import cross_validate

knn_5 = KNeighborsClassifier(n_neighbors=5)
knn_15 = KNeighborsClassifier(n_neighbors=15)

result_5 = cross_validate(knn_5, X_train, y_train, cv=5)
result_15 = cross_validate(knn_15, X_train, y_train, cv=5)

print('Average accuracy across folds (k = 5): {0}.'.format(result_5['test_score'].mean()))
print('Average accuracy across folds (k = 15): {0}.'.format(result_15['test_score'].mean()))
      
knn_5.fit(X_train, y_train)
print('Test dataset accuracy (k = 5): {0}.'.format(knn_5.score(X_test, y_test)))


from sklearn.model_selection import GridSearchCV
# The class GridSearchCV offers a convenient way to choose hyperparameters based on cross-validation
parameters = {'n_neighbors': [1, 3, 5, 7, 9]}

knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, parameters, cv=5)
knn_cv.fit(X_train, y_train)

print('Best hyperparameter setting: {0}.'.format(knn_cv.best_estimator_))
print('Average accuracy across folds of best hyperparameter setting: {0}.'.format(knn_cv.best_score_))
print('Test dataset accuracy of best hyperparameter setting: {0}.'.format(knn_cv.score(X_test, y_test)))
