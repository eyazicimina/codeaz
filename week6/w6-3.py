
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
plt.pie( dwlltype.values(), labels = dwlltype.keys() )
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


