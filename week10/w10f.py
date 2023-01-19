
import pandas as pd

df = pd.read_csv("w10_Mall_Customers.xls")

del df['CustomerID']
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
for c in df:
	if c != 'Gender':
		print(c, df[c].mean(), df[c].std())
		df[c] = (df[c] - df[c].mean()) / df[c].std()

print(df.columns)
print(df)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(df)
print(kmeans.labels_)

df['labels'] = kmeans.labels_

for g in df.groupby('labels'):
	print(g[1].mean().to_dict())
	
import matplotlib.pyplot as plt

df.to_csv("w10f.csv")

plt.scatter( df['Age'], df['Annual Income (k$)'],c = df['labels'] )


plt.show()


# FEATURE SELECTION ==> TARGET YOK, CORRELATION [x > 0.15]   df['x'].corr( df['target'] ) > 0.20
# categoric degiskenler ==> target.avg() == iptal, yok

