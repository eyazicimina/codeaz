import numpy as np
import pandas as pd
path = "/home/mina5/PycharmProjects/codeaz-python/"

def linreg(X, Y):
	"""
	return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
	"""
	N = len(X)
	Sx = Sy = Sxx = Syy = Sxy = 0.0
	for x, y in zip(X, Y):
		Sx = Sx + x
		Sy = Sy + y
		Sxx = Sxx + x*x
		Syy = Syy + y*y
		Sxy = Sxy + x*y
	det = Sxx * N - Sx * Sx
	return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det

#: Read csv
df = pd.read_csv(path + "w10_Electric_Production.csv")

#: Add an index
df['Index'] = range(1, 1+len(df))
#: Get the values
values = df['Value'].values
#: Find the trend
b1, b0 = linreg( range(len(values)), values )
# y = index * b1 + b0
#: Add the trend to dataset
df['Trend'] = df['Index'] * b1 + b0
del df['Index']

df['Lag1'] = df['Value'].shift(1)
df['Lag6'] = df['Value'].shift(6)
df['Lag5'] = df['Value'].shift(5)
df['Lag12'] = df['Value'].shift(12)
# The problem of increasing L:

# Feature generation
df['ma3'] = df['Value'].rolling(3, closed = 'left').mean()
df['ma5'] = df['Value'].rolling(5, closed = 'left').mean()
#: Create a column to forecast "TOMORROW", NOT "TODAY"
df['target'] = df['Value'].shift(-1)
#: Remove the value column (we are not going to use it)
del df['Value']

df = df.dropna()




from sklearn.neural_network import MLPRegressor

dt = df['DATE']
del df['DATE']

train = df[0:335]
test = df[335:]

train_y = train['target']
train_x = train.drop( columns = ['target'] )

test_y = test['target']
test_x = test.drop( columns = ['target'] )


# MLP = HARD complex algortihm
# THIS MEANS IT MAY REQUIRE HUGE AMOUNT OF DATA!!!!!! (10.000 +)
from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor
regr = MLPRegressor(random_state=1, max_iter=500, hidden_layer_sizes=(20,)).fit(train_x, train_y)
regr = RandomForestRegressor(max_depth=4, random_state=0).fit(train_x, train_y)
#regr = LinearRegression().fit(train_x, train_y)
#print(regr.coef_)
#print(regr.intercept_)
print(train_x.columns)

print( regr.score( test_x, test_y ) )

test_x['pred'] = regr.predict( test_x )
test_x['real'] = test_y

print(test_x.shape)

test_x.to_csv(path + "w10results.csv")


