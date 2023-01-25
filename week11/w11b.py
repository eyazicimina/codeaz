# Telecom_customer churn.csv
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA

df = pd.read_csv("w11DR.csv")
target = 'Exited'
del df['Geography']
df['Gender'] = df['Gender'].map({'Female': 1, 'Male': 0})

pca = PCA(n_components=2)
pca.fit( df.drop(columns = ['Exited']) )
pcadata = pca.transform( df.drop(columns = ['Exited']) )
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

