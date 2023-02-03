
import pandas as pd
import numpy as np
df = pd.read_csv("Telecom_customer churn.csv")
print(df)
def gini(actual, pred, cmpcol=0, sortcol=1):
	assert (len(actual) == len(pred))
	all = np.asarray(np.c_[actual, pred, np.arange(len(actual))], dtype=np.float)
	all = all[np.lexsort((all[:, 2], -1 * all[:, 1]))]
	totalLosses = all[:, 0].sum()
	giniSum = all[:, 0].cumsum().sum() / totalLosses

	giniSum -= (len(actual) + 1) / 2.
	return giniSum / len(actual)

df = df.fillna(0)
df = df.select_dtypes(exclude = ['object'])

def gini_normalized(a, p):
	return gini(a, p) / gini(a, a)




print(df['churn'].mean())

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=2, random_state=0)
y =df['churn']
x = df.drop(columns = ['churn'])
clf.fit(x,y)
imp = clf.feature_importances_
index = 0


importances = pd.DataFrame(columns = ['featureName', 'correlation', 'gini', 'featureImportance'])

for col in x:
	try:
		g = gini_normalized(df['churn'], df[col])
		c = abs(df['churn'].corr(df[col]))
		if g > 0.01 and c > 0.01:
			importances.loc[ len(importances) ] = [ col, c, g, imp[index] ]
			print(col, g, c, imp[index] )
	except:
		pass
	index += 1

importances.to_csv("w12_importances.csv")




df['x'].fillna( df['x'].mean()  )