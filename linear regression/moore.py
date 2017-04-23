import numpy as np
import re
import matplotlib.pyplot as plt

regex = re.compile(r'[^\d]+') # non decimal
X, Y = [], []

for line in open('moore.csv'):
	line = line.split('\t')
	x = int(regex.sub('', line[2].split('[')[0])) # the year
	y = int(regex.sub('', line[1].split('[')[0])) # the number of transiters
	X.append(x)
	Y.append(y)


X, Y = np.array(X), np.array(Y)
Y = np.log(Y)

# find out a and b
# copied from lr_1d.py
# denominator = X.dot(X) - X.mean() * X.sum()
# a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator
# b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

####

d = X.mean() * X.mean() - X.dot(X) / len(X)

a = (Y.mean() * X.mean() - X.dot(Y) / len(X)) / d
b = (X.dot(Y) / len(X) * X.mean() - Y.mean() * X.dot(X) / len(X)) / d


Yhat = a * X + b


plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# calculate r-sqaured to see how good is the model
r_squared = 1 - (Y - Yhat).dot(Y - Yhat) / (Y - Y.mean()).dot(Y - Y.mean())
print r_squared
print("time to double " , np.log(2) / a)