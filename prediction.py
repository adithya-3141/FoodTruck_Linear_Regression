
import numpy as np


def prediction(x, theta):

    thetaVector = np.transpose(theta)
    thetaVector = thetaVector.reshape((2,1))
    X = np.array([1, x])
    X = X.reshape((1, 2))
    P = np.matmul(X, thetaVector)
    return P[0][0] * 10000        
