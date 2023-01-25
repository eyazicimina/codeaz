import numpy as np
import math
import random
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA

df = pd.read_csv("Telecom_customer churn.csv")
df = df.select_dtypes(exclude=['object'])
df = df.fillna(df.mean())
target = 'churn'

#: Create a pca component
pca = PCA(n_components=2) # independed from correlations!
pca.fit( df.drop(columns = [target]) )
print( pca.explained_variance_ratio_.cumsum() )
print( pca.explained_variance_ratio_ )

pcadata = pca.transform( df.drop(columns = [target]) )
pcadata = pd.DataFrame(pcadata)
pcadata.columns = ['pca0', 'pca1']


# DISTANCE1 = |a-b|
# DISTANCE2 = |a-c|
# DISTANCE1 < DISTANCE2, a ile b, a ile c ye gore daha yakindir

def euclideandistance( values1, values2 ) -> float:
	if len(values1) != len(values2):
		raise ValueError("Boyutlar esit degildir")

	s = 0
	for i in range(len(values1)):
		s += math.pow(values1[i] - values2[i], 2.0)
	return math.sqrt(s)


def w_euclidean_distance(x, y, w):
	"""Calculates the weighted Euclidean distance between two points

	Args:
			x,y (list): lists of numbers representing the two points
			w (list): list of numbers representing the weights
	Returns:
			float: the weighted Euclidean distance between the two points
	"""

	# Check that x,y, and w are all the same length
	if len(x) != len(y) or len(x) != len(w):

		raise ValueError("x, y and w must all be the same length")

	# Calculate the weighted euclidean distance
	dist = 0
	for i in range(len(x)):
		dist += w[i] * (x[i] - y[i]) ** 2
	dist = dist ** 0.5
	return dist

# HEURISTIC APPROACH!

distances = []
for _ in range(3000):
	r1 = random.randint( 0, len(pcadata) - 1)  # between 0 and length of the dataset
	r2 = random.randint( 0, len(pcadata) - 1)
	row1 = list(dict(pcadata.iloc[r1].to_dict()).values())
	row2 = list(dict(pcadata.iloc[r2].to_dict()).values())
	row2 = [0, 0] # MERKEZ, CENTER, AVERAGE, MEAN
	distance = w_euclidean_distance( row1, row2, list(pca.explained_variance_ratio_) )
	# YARICAP !!
	distances.append( distance )


pcadata[ 'distanceToCenter' ] = pcadata.apply(lambda row: w_euclidean_distance(list(row.to_dict().values()), [0,0], list(pca.explained_variance_ratio_)), axis = 1)

pcadata[ 'yeni-variable' ] = pcadata['pca0'] > 23000

print(pcadata[ pcadata['distanceToCenter'] < 23000 ])
print(pcadata[ pcadata['distanceToCenter'] >= 23000 ])

# ALL COMBINATIONS TAKE TOOOOO LONG TIME
"""
for i1 in range(len(pcadata)):
	for i2 in range(len(pcadata)):
		w_euclidean_distance( i1, i2 )
"""


print(np.max(distances))
print(np.mean(distances))

# sqrt( (42526 - 50016)^2 * 0.83 + (-13378 - 20435)^2 * 0.15 )

print("============================")

# VERI URETMEK
# DATA SYNTHESIS
# DATA GENERATION
# SYNTHETIC DATA GENERATION

# PCA

for _ in range(10000):
	print( pca.inverse_transform( [[random.random() * pcadata['pca0'].mean(), random.random() * pcadata['pca1'].mean()]] ) )

# ========================
#: SIMULASYON
# --> boyle bir durum olusursa ne olur?


# 2. tip veri uretme
# WI analizi
# lda








