import matplotlib.pyplot as plt

def plotData(X, y):
    plt.scatter(X, y, marker= 'x')
    plt.title('Popultion of City vs Profit of Food Truck')
    plt.xlabel('Population')
    plt.ylabel('Profit')
    plt.show()