import matplotlib.pyplot as plt
import numpy as np

def plotData(X, y):
    plt.scatter(X, y, marker= 'x', label = 'Data')
    plt.title('Popultion of City vs Profit of Food Truck')
    plt.xlabel('Population')
    plt.ylabel('Profit')
  


def plotPrediction(X, theta):
    m = X.size
    unitVector = np.ones((m , 1)) 

    X = X.reshape((m,1))
    X = np.hstack((unitVector, X))
    thetaVector = np.transpose(theta)
    thetaVector = thetaVector.reshape((2,1)) 
    hypothesis = np.matmul(X, thetaVector)
    X = X[:, 1]
  
    
    plt.plot(X, hypothesis, 'r', label = "line of best fit")
    plt.legend(loc = "lower right")
    plt.show()