import numpy as np



def gradientDescent(X, y , theta, alpha, iterations):
    
    m = X.size
    y = y.reshape((m,1))   
  
    unitVector = np.ones((m , 1)) 

    X = X.reshape((m,1))
    X_prime = np.hstack((unitVector, X))   
   
    for i in range(iterations):

        thetaVector = np.transpose(theta)      
        thetaVector = thetaVector.reshape((2, 1)) 


        hypothesis = np.matmul(X_prime, thetaVector)

        costTerm = hypothesis-y
        costTranspose = np.transpose(costTerm)

        productTerm = costTerm * X
        productTranspose = np.transpose(productTerm)

        T1 = np.matmul(costTranspose, unitVector)
        T2 = np. matmul (productTranspose,unitVector)

        thetaZero = theta[0] - (alpha/m)*T1[0][0]
        thetaOne = theta[1] - (alpha/m)*T2[0][0]


        theta[0] = thetaZero
        theta[1] = thetaOne
        
       