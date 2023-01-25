#
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

itemsToDelete = []
itemsToReduce = []
for c in df:
	if c != target:
		corr = abs(df[c].corr(df[target]))
		if corr < 0.01:
			itemsToDelete.append( c )
		elif corr < 0.05:
			itemsToReduce.append( c )
		else:
			pass

#: Remove the columns
for c in itemsToDelete:
	del df[c]

#: Create a pca component
pca = PCA(n_components=1)
pca.fit( df[itemsToReduce] )

#: Reduce the dimensions
df['pca0'] = pca.transform( df[itemsToReduce] )

#: Remove the columns
for c in itemsToReduce:
	del df[c]

print("itemsToDelete", itemsToDelete)
print("itemsToReduce", itemsToReduce)
print(df['pca0'].corr( df[target] ))
print(df.columns)
sys.exit(1)
pca = PCA(n_components=2)
pca.fit( df.drop(columns = [target]) )
pcadata = pca.transform( df.drop(columns = [target]) )
pcadata = pd.DataFrame(pcadata)
pcadata.columns = ['pca0', 'pca1']
df['pca0'] = pcadata['pca0']
# df['pca1'] = pcadata['pca1']

print(df.head())
sys.exit(1)

limit = 5000
train = df[:limit]
test  = df[limit:]

train_y = train[target]
train_x = train.drop(columns = [target])

test_y = test[target]
test_x = test.drop(columns = [target])

clf = RandomForestClassifier(max_depth=5, random_state=0)
clf.fit( train_x, train_y )



print("f1", f1_score( test_y, clf.predict(test_x) ) )

