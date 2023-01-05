import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# THE MOST IMPORTANT TOPIC
# 1- Feature Representation, Evaluation
# 2- Feature Extraction & Feature Mining
# 3- Feature Selection [criteria]

# FEATURE = COLUMN = ATTRIBUTE = SUTUN = KOLON

# How do we represent the features
df = pd.read_csv("/home/mina5/PycharmProjects/codeaz-python/Telecom_customer churn.csv")

print(df.dtypes)
print(df.head())
# HOW DO WE REPRESENT CATEGORICAL VARIABLES
# dwllsize

# dwlltype = S, M
# gender = F, M
# ownrent


# FLAG variables, easy, just replace with 1/0
print(df['ownrent'].unique())  # O, R, nan

df['ownrent'] = df['ownrent'].map( {'O': 1, 'R': 0} )
df['ownrent'] = df['ownrent'].fillna(0)
print(df['ownrent'])

# dwllsize

# DEFAULT DUMMY COLUMN GENERATOR
df2 = pd.get_dummies( df, columns=['dwllsize'] )
df2.head(100).to_csv("w8sample.csv")
print(df2.columns)

# getDummiesCA == CodeAcademy
def getDummiesCA(df: pd.DataFrame, column: str, topN: int = 4) -> pd.DataFrame:
	# NOTE: value_counts, gives the values "SORTED" by frequency
	values = dict( df[ column ].value_counts() )
	values = list(values.keys())[0:topN]

	for v in values:
		df[ column + '_' + v ] = df[column].apply( lambda value: 1 if value == v else 0 )

	del df[column]
	return df

def getDummiesProportionCA(df: pd.DataFrame, column: str) -> pd.DataFrame: # FAIZ, ORAN, PERCENTAGE, USAGE RATIO
	# NOTE: value_counts, gives the values "SORTED" by frequency
	values = dict( df[ column ].value_counts() )
	#: From frequency to ratio
	for v in values:
		values[v] = values[v] / len(df)

	df[column] = df[column].map( values )

	return df



def getDummiesTargetCA(df: pd.DataFrame, column: str, target: str) -> pd.DataFrame: # FAIZ, ORAN, PERCENTAGE, USAGE RATIO
	# NOTE: value_counts, gives the values "SORTED" by frequency
	vmap = {}
	for c in df[column].unique():
		vmap[c] =  df[ df[column] == c ][ target ].mean()

	df[ column ] = df[column].map( vmap )

	return df


# grouping



#df = getDummiesProportionCA(df, 'dwllsize')
#df.head(100).to_csv("w8sample.csv")
#print(df)

df = getDummiesTargetCA( df, 'marital', 'churn' )
df.head(10000).to_csv('w8sample.csv')

categorics = []
for c in df:
	if str(df.dtypes[c]) == 'object':
		categorics.append(c)

"""
for c in categorics:
	df = getDummiesTargetCA( df, c, 'churn' )
	print(c, df[c].corr(df['churn']))

"""

# Categoric variables can be represented as "is it the most frequent or not"?
"""
for c in categorics:
	df[ c ] = (df[ c ] == df[c].mode()[0]) # most frequent value
	print(c, df[c].corr(df['churn']))
"""

# How to represent categorical variables:
# dummy
# limited dummy
# proportion
# target
# mode or not
# grouping [1] = business known
# grouping [2] = business unknown
# top most N
# least most N

# BENZER = SIMILAR = benzerlik metrik?


def showSimilarities(df: pd.DataFrame, column: str, target: str) -> pd.DataFrame:

	vmap = {}
	for c in df[column].unique():
		vmap[c] =  df[ df[column] == c ][ target ].mean()

	print(column, vmap)

for c in categorics:
	showSimilarities(df, c, 'churn')


s = 'HHstatin'
g1 = ['C', 'I', 'B']
g2 = ['A', 'G', 'H']
df['HHstatin'] = df['HHstatin'].apply(lambda value: 1 if value in g1 else 0)

# Assignment for afternoon
# for categorical variables, make groups of values to represent those variables
# no business information is known
# use target only


for c in categorics:
	# TOP MOST 3 or not?
	topmost = list( dict(df[c].value_counts()).keys() )[0:3]
	df[ c ] = (df[ c ].isin(topmost)) # most frequent value
	print('topmost', c, df[c].corr(df['churn']))
