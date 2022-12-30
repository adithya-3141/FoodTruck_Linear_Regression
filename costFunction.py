import numpy as np

def J(X, y, theta, m):
    # m is the lenght of the training set
    # theta is the coefficients

    thetaVector = np.transpose(theta)  # Vector of theta

    unitVector = np.ones((m,1))
    X = X.reshape((m,1))             # Converting X to a column vector
    X = np.hstack((unitVector,X))    # Adding X0 to the parameters



   
    hypothesis = np.matmul(X, thetaVector)  # hypothesis function 


    costTerm = hypothesis - y

    costTranspose  = np.transpose(costTerm) # transpose of Cost term

    squaredError = np.matmul(costTerm, costTranspose) # square of the cost terms 
    

    return (1/(2*m))*squaredError