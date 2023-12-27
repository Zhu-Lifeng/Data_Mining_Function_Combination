from sklearn.decomposition import PCA

numComponents = 2
pca = PCA(n_components=numComponents)
pca.fit(imgData)
# imgData is a muti-attribute set with huge number of attributes
projected = pca.transform(imgData)
projected = pd.DataFrame(projected,columns=['pc1','pc2'],index=range(1,numImages+1))

pcaNT=PCA()
pcaNT.fit(X_strain_name)
cumulative_variance_ratio = pcaNT.explained_variance_ratio_.cumsum()
nsNT=0
niNT=0
for i,value in enumerate(cumulative_variance_ratio):
    if abs(value-0.8)<abs(nsNT-0.8):
        nsNT=value
        niNT=i
nearestNT=cumulative_variance_ratio[niNT]*100
# this is the information gain ratio of niNT(the component number)
# find the fit number of components with the cumulative_variance_ratio (in this case retain 80% of the information)

columns=[f'Name_{i}' for i in range(1,niNT+1)]
# spare part of column name, it generates column names based on the number of the number of components

# the number of columns must match the value of numComponents
projected['tag'] = df['tag']
