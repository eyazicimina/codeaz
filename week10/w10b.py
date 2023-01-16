from sklearn.metrics import f1_score
import sys
import pandas as pd
path = "/home/mina5/Downloads/codeacedemy/"

df = pd.read_csv(path + "week6-quiz1.csv")
df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes': 1, 'No': 0})
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

# df['Vehicle_Age'] = df['Vehicle_Age'].map({'1-2 Year': 1, '> 2 Years': 2, '< 1 Year': 0})
df = pd.get_dummies( df, columns = ['Vehicle_Age'])

df['var1'] = (df['Previously_Insured'] == 0) & (df['Vehicle_Damage'] == 1)
df['var1'] = df['var1'].astype(int)
df['var2'] = df['Previously_Insured'] * df['Vehicle_Age_1-2 Year']
df['var3'] = df['Previously_Insured'] * df['Vehicle_Age_< 1 Year']
df['var4'] = df['Previously_Insured'] * df['Vehicle_Age_> 2 Years']
df['var8'] = df['Vehicle_Damage'] * df['Vehicle_Age_1-2 Year']
df['var9'] = df['Vehicle_Damage'] * df['Vehicle_Age_< 1 Year']







print( df['Response'].value_counts() )


print(df.columns)
print(df.shape)

# Gender  Age  Driving_License  ...  Policy_Sales_Channel  Vintage Response
"""
Index(['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured',
       'Vehicle_Age', 'Vehicle_Damage', 'Annual_Premium',
       'Policy_Sales_Channel', 'Vintage', 'Response'],
      dtype='object')
"""
target = 'Response'
df = df.select_dtypes(exclude=['object'])
df = df.sample(n = 100000)

limit = int(0.70 * len(df))
train = df[:limit]

# rebalancing, tekrar dengeleme
birler = train[ train['Response'] == 1 ]
sifirlar = train[ train['Response'] == 0 ].sample(frac = 0.40) # 0.19 @ 0.40 ==> f1:0.42

train = pd.concat([  birler, sifirlar ])
train = train.sample(frac = 1.0)

test  = df[limit:]

train_y = train[target]
train_x = train.drop(columns = [target])

test_y = test[target]
test_x = test.drop(columns = [target])

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=6, random_state=0)
# CHANGE ALGO, CHANGE PARAMS

clf.fit(train_x, train_y) # TRAIN, OGRENME

print("score", clf.score( test_x, test_y ))
tahmin = clf.predict( test_x ) # USE, KULLAN, INFER
olasilik = clf.predict_proba( test_x )[:,1] # USE, KULLAN, INFER
print("f1", f1_score( test_y, tahmin ) )
print(tahmin, tahmin.shape)

test_x['tahmin'] = tahmin
test_x['gercek'] = test_y
test_x['sonuc'] = test_x['gercek'] == test_x['tahmin']
test_x['tahmin-metinsel'] = test_x['tahmin'].apply(lambda value: "POSITIVE" if value == 1 else "NEGATIVE")
test_x['olasilik'] = olasilik


COST_MATRIX = {
	'TP': 450,
	'TN': 50,
	'FP': 50,
	'FN': 500,
}


def agirlikliDogrulukHesapla(test_x) -> float:
	total = 0
	trues = 0
	for c in COST_MATRIX:
		total += COST_MATRIX[c] * test_x[c].sum()
		if c[0] == 'T':
			trues += COST_MATRIX[c] * test_x[c].sum()
	return trues / total



for i in range(0, 100, 5):
	value = float(i) / 100.0
	pass


eniyidogruluk = 0
eniyiesik = 0
esik_degerleri = [0.05 + 0.05 * i for i in range(19)]
for t in esik_degerleri:
	test_x['tahmin'] = test_x['olasilik'] > t
	test_x['TP'] = test_x.apply(lambda row: 1 if row['tahmin'] == 1 and row['gercek'] == 1 else 0, axis = 1)
	test_x['TN'] = test_x.apply(lambda row: 1 if row['tahmin'] == 0 and row['gercek'] == 0 else 0, axis = 1)
	test_x['FP'] = test_x.apply(lambda row: 1 if row['tahmin'] == 1 and row['gercek'] == 0 else 0, axis = 1)
	test_x['FN'] = test_x.apply(lambda row: 1 if row['tahmin'] == 0 and row['gercek'] == 1 else 0, axis = 1)
	dogruluk = agirlikliDogrulukHesapla( test_x )
	print( t, "agirlikliDogrulukHesapla", dogruluk )
	if dogruluk > eniyidogruluk:
		eniyidogruluk = dogruluk
		eniyiesik = t

print("EN IYI", eniyidogruluk, eniyiesik)

"""
for i in range(-5, 5):
	inceayar = float(i) / 100.0
	yeniesik = eniyiesik + inceayar

	test_x['tahmin'] = test_x['olasilik'] > yeniesik
	test_x['TP'] = test_x.apply(lambda row: 1 if row['tahmin'] == 1 and row['gercek'] == 1 else 0, axis = 1)
	test_x['TN'] = test_x.apply(lambda row: 1 if row['tahmin'] == 0 and row['gercek'] == 0 else 0, axis = 1)
	test_x['FP'] = test_x.apply(lambda row: 1 if row['tahmin'] == 1 and row['gercek'] == 0 else 0, axis = 1)
	test_x['FN'] = test_x.apply(lambda row: 1 if row['tahmin'] == 0 and row['gercek'] == 1 else 0, axis = 1)
	dogruluk = agirlikliDogrulukHesapla( test_x )
	print( yeniesik, "agirlikliDogrulukHesapla", dogruluk )
"""

test_x['tahmin'] = test_x['olasilik'] > eniyiesik
test_x['tahmin'] = test_x['tahmin'].astype(int)
test_x['TP'] = test_x.apply(lambda row: 1 if row['tahmin'] == 1 and row['gercek'] == 1 else 0, axis=1)
test_x['TN'] = test_x.apply(lambda row: 1 if row['tahmin'] == 0 and row['gercek'] == 0 else 0, axis=1)
test_x['FP'] = test_x.apply(lambda row: 1 if row['tahmin'] == 1 and row['gercek'] == 0 else 0, axis=1)
test_x['FN'] = test_x.apply(lambda row: 1 if row['tahmin'] == 0 and row['gercek'] == 1 else 0, axis=1)


test_x.to_csv(path + "w10output.csv")

dogrubildiklerimiz = test_x[ test_x['tahmin'] == test_x['gercek'] ]
yanlisbildiklerimiz = test_x[ test_x['tahmin'] != test_x['gercek'] ]

dogrubildiklerimiz = dogrubildiklerimiz.mean().to_dict()
yanlisbildiklerimiz = yanlisbildiklerimiz.mean().to_dict()

farklar = {}
for x in dogrubildiklerimiz:
	mape = abs( dogrubildiklerimiz[x] - yanlisbildiklerimiz[x] ) / ( dogrubildiklerimiz[x] + yanlisbildiklerimiz[x] )
	if mape > 0.1:
		farklar[x] = mape


print(farklar)



test_x.to_csv(path + "w10output.csv")


# Filling
# Data cleaning
# Normalization
# Feature mining
# Threshold



# !Different algorithms
# !Different parameters
# !Different approach (voting)