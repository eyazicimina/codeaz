import random
import pandas as pd
import sys
df = pd.read_csv("w10_customers.csv")

del df['Region']
#df['Region'] = df['Region'] == 3
#df['Region'] = df['Region'].astype(int)

df['Channel'] = df['Channel'] == 1
df['Channel'] = df['Channel'].astype(int)

for c in ['Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicatessen']:
	df[c] = (df[c] - df[c].mean()) / df[c].std()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, random_state=0, n_init="auto").fit(df)
print(kmeans.labels_)

df['labels'] = kmeans.labels_

# 3 ==> 1.17
# 4 ==> 1.70
# 5 ==> 4.83
# 6 ==> 3.66

# max( between )
# min( within )

centroids = {}


for g in df.groupby('labels'): # split the dataframe into sub categories according to "LABELS"
	groupindex = g[0]
	groupdataframe = g[1]
	d = dict(groupdataframe.mean().to_dict())
	del d['labels']
	centroids[ groupindex ] = d

metric1 = 0


import numpy as np

def euclidean_distance(x,y):
  return np.linalg.norm(x-y)


import itertools
columns = list(centroids.keys())
combinations = list(itertools.combinations(columns, 2))


distances = []
for c in combinations:
	first = c[0]
	second = c[1]
	dis = euclidean_distance(np.array(list(centroids[ first ].values())), np.array(list(centroids[ second ].values())) )
	distances.append( dis )
print(combinations)
print(distances)


between_distance = np.mean( distances )
print("between_distance of clusters", between_distance) # ne kadar buyukse o kadar iyi!!!!

# =======================================
withindistances = []


for g in df.groupby('labels'):
	groupindex = g[0]
	groupdataframe = g[1]
	del groupdataframe['labels']

	ingroupdistances = []
	for i in range(10): # RANDOMLY SELECT 10 ITEMS
		index1 = random.randint(0, len(groupdataframe) - 1)
		index2 = random.randint(0, len(groupdataframe) - 1)
		d = euclidean_distance( np.array(list(groupdataframe.iloc[index1].to_dict().values())), np.array(list(groupdataframe.iloc[index2].to_dict().values()))  )
		ingroupdistances.append( d )

	ingroupdistances = np.mean( ingroupdistances )
	withindistances.append( ingroupdistances )


within_distance = np.mean(withindistances)
print("within_distance", within_distance) # minimum is better, ne kadar kucuksa o kadar iyi

print( between_distance / within_distance )

