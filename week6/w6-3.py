
import os

file_path = os.path.realpath(__file__)
print(file_path)
print(r'/home/mina5/PycharmProjects/codeaz-python/telcochurn.csv')
import pandas as pd
dx = pd.read_csv(r'/home/mina5/PycharmProjects/codeaz-python/telcochurn.csv')
#dx = dx.sample(15000)

#! dx.isna().to_csv('/home/mina5/PycharmProjects/codeaz-python/w6_TF.csv')
dx.isna().corr().to_csv('/home/mina5/PycharmProjects/codeaz-python/w6_TF.csv')

print(dx.shape)

# METHOD 1: REMOVE THE ITEMS WITH NULL VALUES
# METHOD 2: FILLING (fill them with appropriate values)
# METHOD 3: DIVIDE INTO TWO DIFFERENT DATASETS

dx = dx[ dx['rev_Mean'].notnull() ]
dx = dx[ dx['ethnic'].notnull() ]

# --- FILL
# avg6mou	avg6qty	avg6rev
# print(dx[  dx['avg6mou'].isna() ] )

print(dx.isna())

print(dx.describe(include = 'all').T.to_csv("/home/mina5/PycharmProjects/codeaz-python/w6_desc.csv"))
print(dx.shape)


# 2.A: Fill with zero?
#! dx['numbcars'] = dx['numbcars'].fillna(  0  )
# 2.B: Fill with "MEAN"
#! dx['numbcars'] = dx['numbcars'].fillna(  dx['numcars'].mean() )
# 2.C: Discrete -- Categoric, Mode
dx['numbcars'] = dx['numbcars'].fillna(  dx['numbcars'].mode()[0] )

dx['ownrent'] = dx['ownrent'].fillna( 'O' )

dx['HHstatin'] = dx['HHstatin'].fillna('C')

dwlltype = dx['dwlltype'].value_counts().to_dict()
total = sum(dwlltype.values())
print(dwlltype, total)

#: TRANSFORM INTO RATIO
for c in dwlltype:
	dwlltype[c] = dwlltype[c] / total

print(dwlltype)

import matplotlib.pyplot as plt
#! plt.pie( dwlltype.values(), labels = dwlltype.keys() )
#plt.show()


# !  fill:  constant (0)
# !  fill:  different values?
# for a new record, what is the probability of the row belongs to "S" ? ===> 0.71 %71

import random


randomList = random.choices(['S', 'M'], weights=(71, 29), k=1000)
print(randomList.count('S'))
"""
#for _ in range(100):
#	print(random.choice(['S','M']))
	r = random.random()
	if r < 0.7160391954615781:
		print('S')
	else:
		print('M')
"""


df = pd.read_csv("/home/mina5/PycharmProjects/codeaz-python/w6_e-commerce.csv", encoding='latin-1')
df['CustomerID'] = df['CustomerID'].astype(str)
df2 = pd.DataFrame(columns = ['CustomerID', 'Products'])

for a in df.groupby(['CustomerID']):

	df2.loc[ len(df2) ] = [ a[0], a[1]['StockCode'].unique() ]
	#print(a[0]) # -- customerId
	#print(a[1]['StockCode'].unique()) # dataframe (df[ df['customerId] == a[0] ]

print(df2)

#: Get random indexes
ind0 = random.randint( 0, len(df2) - 1 )
ind1 = random.randint( 0, len(df2) - 1 )

#: Get the rows
row0 = list(df2.iloc[ ind0 ]['Products'])
row1 = list(df2.iloc[ ind1 ]['Products'])


def jaccard( l0, l1 ):
	return len(set(l0).intersection(set(l1))) / len(set(l0).union(set(l1)))


print(row0, type(row0))
print(row1, type(row1))

print(jaccard( row0, row1 ))

# ASSIGNMENT: 22 DECEMBER, Find the most similar customers by their bought products


# ALTERNATIVE APPROACH TO FILL CATEGORICAL VALUES
# random.choice( list( dx[ dx['ownrent'].notnull() ]['ownrent'].values ) )
# R ve O gelme probability

# AFTER NOON ASSIGNMENT 2:
# Use the expression below to fill the dataset
# random.choice( list( dx[ dx['ownrent'].notnull() ]['ownrent'].values ) )

"""
list( dx[ dx['ownrent'].notnull() ]['ownrent'].values ) # liste cevrilmis hali
dx[ dx['ownrent'].notnull() ]['ownrent'].values # null olmayan kayitlarin ownrent kolonundaki valuelar
dx[ dx['ownrent'].notnull() ]['ownrent'] # null olmayan kayitlarin ownrent kolonu
dx[ dx['ownrent'].notnull() ] # null olmayan kayitlar
dx['ownrent'].notnull()  # null olmayanlar
"""


# FILLING NUMERICAL VARIABLES
# ? mean XXX
#   median XXX
import numpy as np
mu, sigma = dx['hnd_price'].mean(), dx['hnd_price'].std() # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
plt.hist(s)
#plt.show()
print(np.mean(s), np.std(s))
print(dx['hnd_price'].describe())



