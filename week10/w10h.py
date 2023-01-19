

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

from sklearn.cluster import DBSCAN
clustering = DBSCAN(eps=1, min_samples=4).fit(df)
labels = list(clustering.labels_)

df['labels'] = labels
import collections
counter = collections.Counter(labels)
print(counter)


for g in df.groupby( 'labels' ):
	print(g[1].mean().to_dict())


# K-MEANS ==> MUST ASSIGN EVERY ITEM TO A CENTROID!!!
# DB SCAN CLUSTERING ==> NOT REALLY NECESSARY
