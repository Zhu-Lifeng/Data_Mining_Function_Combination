from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100, random_state=0)
rfc.fit(X_train, y_train)
print(rfc.score(X_test, y_test))
print('Test dataset accuracy (random forest classifier): {0}.'.format(rfc.score(X_test, y_test)))
