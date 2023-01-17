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
#: Make it detrend
df['Detrend'] = df['Value'] - df['Trend']
#: Lag
d2 = pd.DataFrame(columns = ['Value', 'Lag1', 'Lag3'])
for i in range(3, len(df)):
	l3 = df.iloc[i-3]['Value']
	l1 = df.iloc[i-1]['Value']
	l0 = df.iloc[i]['Value']

	d2.loc[ len(d2) ] = [l0, l1, l3]

df['Lag1'] = df['Value'].shift(1)
df['Lag6'] = df['Value'].shift(6)
df['Lag5'] = df['Value'].shift(5)
df['Lag12'] = df['Value'].shift(12)
# The problem of increasing L:
# (1) 12 rows will be deleted !! L = 24, 24 rows will be deleted
# (2) It may show the data is correlated, but as the new data comes, the correlation may drop (L = 60, 2months)




#: Auto correlation
for i in range(1, 31):
	print(i, df['Value'].corr( df['Value'].shift(i)  ))

print(df.shape, df.columns)

#: Moving average
d3 = pd.DataFrame(columns = ['Value', 'ma3'])
for i in range(3, len(df)):
	l3 = df.iloc[i-3]['Value']
	l2 = df.iloc[i-2]['Value']
	l1 = df.iloc[i-1]['Value']

	ma3 = np.mean( [l1, l2, l3] )

	l0 = df.iloc[i]['Value']
	d3.loc[ len(d3) ] = [ l0, ma3 ]

print(d3)

# Feature generation
df['ma3'] = df['Value'].rolling(3, closed = 'left').mean()
df['ma5'] = df['Value'].rolling(5, closed = 'left').mean()

df = df.dropna()
print(df)

df.to_csv(path + 'w10timeseries.csv')

from sklearn.neural_network import MLPRegressor

train = df[0:300]
test = df[300:]

train_y = train['Value']
train_x = train.drop( columns = ['Value'] )

test_y = test['Value']
test_x = test.drop( columns = ['Value'] )


regr = MLPRegressor(random_state=1, max_iter=500).fit(train_x, train_y)
regr.score( test_x, test_y )