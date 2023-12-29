from scipy.spatial import distance
import numpy as np

dist = distance.squareform(distance.pdist(X))
# pdist computes pairwise Euclidean distances between samples in the table
# squareform turns the pdist result into a square matrix representation (pdist returns a condensed representation of a symmetric)


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

# Mahalanobis distance: the distance between a point and a distribution
