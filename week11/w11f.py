import warnings
warnings.filterwarnings("ignore")
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

limit = 50000
train = df[:limit]
test  = df[limit:]

train_y = train[target]
train_x = train.drop(columns = [target])

test_y = test[target]
test_x = test.drop(columns = [target])

clf = RandomForestClassifier(max_depth=5, random_state=0)
clf.fit( train_x, train_y )



print("f1", f1_score( test_y, clf.predict(test_x) ) )

churn_edecek_bir_musteri = None

for _ in range(10):
	r = random.randint(0, len(test_x) - 1)
	row = test_x.iloc[ r ]

	result = clf.predict( [row] )[0]
	if result == 1:
		churn_edecek_bir_musteri = row
		break


print("churn_edecek_bir_musteri", churn_edecek_bir_musteri.to_dict())
# NE YAPARSAM, CHURN ETMEZ?


for c in df.select_dtypes(exclude = ['object']).columns:
	if c != "churn":
		churn_edecek_bir_musteri_updated = churn_edecek_bir_musteri.copy()
		churn_edecek_bir_musteri_updated[c] *= 1.5
		result = clf.predict( [churn_edecek_bir_musteri_updated] )[0]
		if result == 0:
			print("BULDUK")
			print(c)
			print(churn_edecek_bir_musteri)
			print(churn_edecek_bir_musteri_updated)

for c in df.select_dtypes(exclude = ['object']).columns:
	if c != "churn":
		churn_edecek_bir_musteri_updated = churn_edecek_bir_musteri.copy()
		churn_edecek_bir_musteri_updated[c] *= 0.5
		result = clf.predict( [churn_edecek_bir_musteri_updated] )[0]

		if result == 0:
			print("BULDUK")
			print(c)
			print(churn_edecek_bir_musteri)
			print(churn_edecek_bir_musteri_updated)
