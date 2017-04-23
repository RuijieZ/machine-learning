import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

# read input for the csv file
for line in open("data_1d.csv"):
	x, y = line.split(',')[0], line.split(',')[1]
	X.append(float(x))
	Y.append(float(y))

# create numpy array
X = np.array(X)
Y = np.array(Y)
N = len(X)

# caculate a and b
barX = X.mean()
barY = Y.mean()
barXY = np.dot(X, Y) / N
barXSquared = np.dot(X, X) / N

d = barX ** 2 - barXSquared

a = (barY * barX - barXY) / d
b = (barXY*barX - barY * barXSquared) / d

newY = a * X + b

# plot the graph
plt.scatter(X, Y)
plt.plot(X, newY)
plt.show()

# calculate r-squared


r_squared = 1 - np.dot(Y - newY, Y -newY) /  np.dot(Y - Y.mean(), Y - Y.mean())

print r_squared 