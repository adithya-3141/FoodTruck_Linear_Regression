import numpy as np
from plotData import plotData
from plotData import plotPrediction
from costFunction import J
from gradientDescent import gradientDescent
from prediction import prediction



data = np.genfromtxt('data.txt', delimiter = ',')

X = data[:, 0] # Input parameters
y= data[:,1] # Output Values
theta = [0 , 0 ]

plotData(X, y)

j = J(X, y, theta, X.size)


alpha = 0.01
iterations  = 1500
gradientDescent(X, y, theta, alpha, iterations)
print(theta)


plotPrediction(X, theta)



predictedValue = prediction(7, theta)
print(predictedValue)








