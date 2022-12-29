import numpy as np
from plotData import plotData
from costFunction import J



data = np.genfromtxt('data.txt', delimiter = ',')

X = data[:, 0] # Input parameters
y= data[:,1] # Output Values
theta = [0,0]


j = J(X, y, theta, X.size)

print(j)
#plotData(X, y)



