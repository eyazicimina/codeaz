import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = "/home/mina5/PycharmProjects/codeaz-python/"




def dayOfYear( dto ):
	return float(dto.timetuple().tm_yday) / 366.0

def daylengthGT( dto, limit: int ) -> float:
	return daylength( dto ) > limit

# method: daylength
# Computes the length of the day
# @dayOfYear, int: The day of the year. 1 corresponds to 1st of January
# @lat, float: Latitude of the location in degrees. Positive values for north and negative for south.
# @return, float: The length of the day in hours
# @completed
def daylength(dto, lat:float = 41.01) -> float:
	dayofyear = dayOfYear( dto ) * 366.0
	"""Computes the length of the day (the time between sunrise and
	sunset) given the day of the year and latitude of the location.
	Function uses the Brock model for the computations.
	For more information see, for example,
	Forsythe et al., "A model comparison for daylength as a
	function of latitude and day of year", Ecological Modelling,
	1995.
	Parameters
	----------
	"""
	latInRad = np.deg2rad(lat)
	declinationOfEarth = 23.45*np.sin(np.deg2rad(360.0*(283.0+dayofyear)/365.0))
	if -np.tan(latInRad) * np.tan(np.deg2rad(declinationOfEarth)) <= -1.0:
		return 24.0
	elif -np.tan(latInRad) * np.tan(np.deg2rad(declinationOfEarth)) >= 1.0:
		return 0.0
	else:
		hourAngle = np.rad2deg(np.arccos(-np.tan(latInRad) * np.tan(np.deg2rad(declinationOfEarth))))
		return 2.0*hourAngle/15.0


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


df = pd.read_csv(path + "w10_train_6BJx641.csv")
# pressure
# electricity_consumption


df['temperature'] = (df['temperature'] - df['temperature'].mean()) / df['temperature'].std()
#df['pressure'] = (df['pressure'] - df['pressure'].mean()) / df['pressure'].std()
#df['electricity_consumption'] = (df['electricity_consumption'] - df['electricity_consumption'].mean()) / df['electricity_consumption'].std()
#df['windspeed'] = (df['windspeed'] - df['windspeed'].mean()) / df['windspeed'].std()
#plt.plot(df['electricity_consumption'])

target = 'electricity_consumption'


a, b = linreg( range(len(df)), df[target] )
trendline = [-0.12707578385951898 + i * 9.592435090358075e-06 for i in range(len(df))]
#plt.plot(trendline)
plt.plot(df[target])


best = 0
bestAt = 0
for i in [1,2,3,4,5,6,7,8,9,10,11,12,24]: #[24, 7 * 24, 24 * 30, 24 * 30 * 3, 24 * 30 * 6]:
	b = df[target].corr( df[target].shift(i) )

# plt.show()
# business department == 8 hours !!
# minimum = 4
# 4,5,6,7,8

del df['temperature']
del df['pressure']
del df['windspeed']
del df['var1']

# Feature generation
df[target] = df[target] - df[target].mean()
# MOVING AVERAGE
for m in [2,3,4,5,6,12,24]: df['ma' + str(m)] = df[target].rolling(m, closed = 'left').mean()
# LAGGED DATA
for l in [4, 5, 6, 7, 8, 12, 24, 48 ]: df['lag' + str(l)] = df[target].shift(l)
# TREND
df['index'] = [i for i in range(len(df))]
df['trend'] = 1.66 + df['index'] * -0.0001
del df['index']
# DATE
df['datetime'] = pd.to_datetime( df['datetime'] )
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['lastdays'] = df['day'] > 20
df['firstdays'] = df['day'] < 5
df['weekday'] = df['datetime'].dt.weekday
df['weekend'] = df['weekday'].isin([5,6])
df['season'] = df['month'].map({ 12:'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6:
																 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'})

df['quarter'] = df['month'].map({ 1: 'q1', 2: 'q1', 3: 'q1', 4: 'q2', 5: 'q2', 6: 'q2',
																		7: 'q3', 8: 'q3', 9: 'q3', 10: 'q4', 11: 'q4', 12: 'q4'})
df['hour'] = df['datetime'].dt.hour
df['noon'] = df['hour'].isin([11,12,13])
df['morning'] = df['hour'].isin([8,9,10])
df['early'] = df['hour'].isin([6,7])
df['afternoon'] = df['hour'].isin([14,15,16,17])
df['evening'] = df['hour'].isin([18,19,20])
df['late'] = df['hour'].isin([21,22])
df['midnight'] = df['hour'].isin([23,0,1])
df['night'] = df['hour'].isin([2,3,4,5])
df['daylength'] = df['datetime'].apply(lambda value: daylength(value))
#: Remove the date time
del df['datetime']
#: Convert into dummies
df = pd.get_dummies(df, columns=['month'])
df = pd.get_dummies(df, columns=['day'])
df = pd.get_dummies(df, columns=['quarter'])
df = pd.get_dummies(df, columns=['weekday'])
df = pd.get_dummies(df, columns=['season'])
#: Remove low correlated variables

#: CHANGE THE TARGET
df[ target ] = df[ target ].shift(-4) # 8 hours LATER
#: DROP NA
df = df.dropna()
#: EXTRA FEATURE MINING
for c in df:
	cc = abs( df[target].corr(df[c]) )
	if cc < 0.10:
		del df[c]


import itertools
columns = [c for c in df.columns if c != target]
combinations = list(itertools.combinations(columns, 2))


index = 0
variables = {}
for c in combinations:
	c1 = c[0]
	c2 = c[1]

	o1 = abs(df[target].corr(df[c1]))
	o2 = abs(df[target].corr(df[c2]))

	df['vara' + str(index)] = df[c1] + df[c2]
	df['varb' + str(index)] = df[c1] * df[c2]
	df['varc' + str(index)] = df[c1] - df[c2]

	variables[ 'vara' + str(index) ] = f"{c1}+{c2}"
	variables[ 'varb' + str(index) ] = f"{c1}*{c2}"
	variables[ 'varc' + str(index) ] = f"{c1}-{c2}"

	corr1 = abs(df['vara' + str(index)].corr(df[target]))
	corr2 = abs(df['varb' + str(index)].corr(df[target]))
	corr3 = abs(df['varc' + str(index)].corr(df[target]))

	if corr1 < 0.10 + o1 or corr1 <0.10 + o2:
		del df['vara' + str(index)]
	if corr2 < 0.10 +o1 or corr2 <0.10 + o2:
		del df['varb' + str(index)]
	if corr3 < 0.10 +o1 or corr3 < 0.10 +o2:
		del df['varc' + str(index)]




	index += 1

for c in df:
	cc = abs( df[target].corr(df[c]) )
	if cc < 0.10:
		del df[c]
	else:
		if c in variables:
			print("A USEFUL COLUMN", c, cc, variables[ c ])


"""
index = 0
for c1 in df:
	for c2 in df:
		if c1 > c2 and c1 != target and c2 != target and not c1.startswith('var') and not c2.startswith('var'):
			df['vara' + str(index)] = df[c1] + df[c2]
			df['varb' + str(index)] = df[c1] * df[c2]
			df['varc' + str(index)] = df[c1] - df[c2]
			index += 1
"""



from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


limit = int(0.70 * len(df))
df = df.sample(frac = 1.0) # Shuffle
train = df[0:limit]
test = df[limit:]

#!!!!! train = df.sample( frac = 0.70)
#!!!!! test =  df.sample( frac = 0.30)

train_y = train[target]
train_x = train.drop( columns = [target] )

test_y = test[target]
test_x = test.drop( columns = [target] )

#regr = MLPRegressor(random_state=1, max_iter=50, hidden_layer_sizes=(50,)).fit(train_x, train_y)
regr = RandomForestRegressor(max_depth=4, random_state=0).fit(train_x, train_y)
#regr = LinearRegression().fit(train_x, train_y)

print(regr.score( test_x, test_y ))
print(df.shape)

test_x['pred'] = regr.predict( test_x )
test_x['real'] = test_y

test_x.to_csv(path + "w10e.csv")