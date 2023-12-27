from scipy.spatial import distance

dist = distance.squareform(distance.pdist(X))
# pdist computes pairwise Euclidean distances between samples in the table
# squareform turns the pdist result into a square matrix representation (pdist returns a condensed representation of a symmetric)
