def mahalanobis(x=None, data=None):
    """Compute the Mahalanobis Distance between each row of x and the data  
    x    : vector or matrix of data with, say, p columns.
    data : ndarray of the distribution from which Mahalanobis distance of each observation of x is to be computed.
    """
    x_mu = x - np.mean(data)
    cov = np.cov(data.values.T)
    inv_covmat = np.linalg.inv(cov)
    left = np.matmul(x_mu, inv_covmat)
  # in this case we assume the data follow a Gussian distribution
    mahal = np.dot(left, x_mu.T)
    return mahal.diagonal()
  

mahal = mahalanobis(x=delta, data=delta[['A', 'B', 'C']])
outlier_score=pd.DataFrame(mahal, index=df.index,columns=['Outlier Score'])
result = pd.concat((delta,outlier_score), axis=1)
result.nlargest(5,'Outlier score')
# get the samples whose outlier scores are higher than 5
