import sys
import pandas as pd
path = "/home/mina5/PycharmProjects/codeaz-python/w12/"
df = pd.read_csv(path + "raw_sales.csv")
df['datesold'] = pd.to_datetime( df['datesold'] )
# print( df['datesold'].value_counts().to_dict() )

df['year'] = df['datesold'].dt.year
df['month'] = df['datesold'].dt.month
df['day'] = df['datesold'].dt.day

df['block'] = df['day'].apply(lambda value: 1 if value < 15 else 0)
# df['block'] = df['day'].apply(lambda value: 1 if value < 10 else (2 if value < 20 else 3))

df = df.sort_values(['year', 'month', 'block'])

df = df.groupby(['year', 'month', 'block']).size()
df = df.reset_index()

# df['newdateblock'] =


#timeseries = df.groupby('datesold').agg({'datesold':'count'})
#print(timeseries, len(timeseries))

df = df.rename(columns = {0: 'value'})
df.to_csv(path + "SIRALI.csv")


df = df[150:]



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

print( df['value'].describe() )

m, n = linreg(range(len(df)), df['value'])

# (0.2521094376093712, 11.055823317674333)
# y = mx + n

df['x'] = range(len(df))
df['trend'] = m * df['x'] + n
df['normalized'] = df['value'] - df['trend']
print(df)

df.to_csv(path + "SIRALI.csv")

for i in range(38):
	c = df['normalized'].corr( df['normalized'].shift(i) )
	if abs(c) > 0.50:
		print(i, c)

import matplotlib.pyplot as plt


for i in range(2, 20):
	df['Lag' + str(i)] = df['normalized'].shift(i)

df['Lag36'] = df['normalized'].shift(36)

trend = df['trend']
del df['value']
del df['trend']
# del df['block']
# del df['year']
#del df['month']


#df['is35'] = df['x'].apply(lambda value: 1 if value % 35 == 0 else 0)
#df['is36'] = df['x'].apply(lambda value: 1 if value % 36 == 0 else 0)
#df['is37'] = df['x'].apply(lambda value: 1 if value % 37 == 0 else 0)


means = df.groupby('year').agg({'normalized': 'mean'}).to_dict()['normalized']
#df['yearavg'] = df['year'].map( means )
df = pd.get_dummies(df, columns = ['year'])

means = df.groupby('month').agg({'normalized': 'mean'}).to_dict()['normalized']
df['monthavg'] = df['month'].map( means )
#df = pd.get_dummies(df, columns = ['month'])


#print(means)
#print("corr", df['yearavg'].corr(df['normalized']))
#sys.exit(1)
df = df.dropna()


from sklearn.linear_model import LinearRegression


y = df['normalized']
print(df.columns)
x = df.drop(columns = ['normalized'])
reg = LinearRegression()
reg.fit(x, y)
print( reg.score(x, y) )


from sklearn.cross_decomposition import PLSRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
pcr = make_pipeline(StandardScaler(), PCA(n_components=5), LinearRegression())
pcr.fit(x, y)

pls = make_pipeline(StandardScaler(), PLSRegression(n_components=4))
pls.fit(x, y)
print( "PCR", pcr.score(x, y) )
print( "PLS", pls.score(x, y) )

sys.exit(1)




df['predict'] = reg.predict( x )
df['real'] = y
df['trend'] = trend

df['real'] = df['real'] + df['trend']
df['predict'] = df['predict'] + df['trend']

df['error'] = df['predict'] - df['real']

plt.plot( df[['real', 'predict', 'error']] )
plt.show()


print(reg.coef_)

df.to_csv(path + "SIRALI.csv")


"""
class Emre:

	def a(self, param):
		return self

	def b(self, param):
		return self


e = Emre()
e.a().b()
"""
