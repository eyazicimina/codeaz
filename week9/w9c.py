import sys
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
path = "/home/mina5/PycharmProjects/codeaz-python/"
df = pd.read_csv(path + "w9_Churn_Modelling.csv")

"""
for c in df:
	print(c, list(df[c].unique())[0:5])

from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile.to_file(path + "w9.html")
"""

print(df.columns)
"""
(['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
       'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
       'Exited'],
      dtype='object')
"""

def featureMiningScalar( df: pd.DataFrame, col: str ) -> pd.DataFrame:
	df[col + '_log' ] = np.log(df[col])
	df[col + '_sqrt' ] = np.sqrt(df[col])
	df[col + '_round' ] = np.round(df[col])
	df[col + '_gtmean' ] = df[col] > df[col].mean()
	df[col + '_gtmean'] = df[col + '_gtmean' ].astype(int)
	df[col + '_gtq3' ] = df[col] > df[col].quantile(0.75)
	df[col + '_gtq3'] = df[col + '_gtq3' ].astype(int)
	df[col + '_pow01' ] = np.power(df[col], 0.1)
	df[col + '_pow20' ] = np.power(df[col], 2.0)
	df[col + '_sign' ] = np.sign(df[col]) # balance = %36 ==> 0, diger value

	return df


for c in ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']:
	df = featureMiningScalar( df, c )

df['Gender'] = df['Gender'].map( {'Female': 1, 'Male': 0} )
df = pd.get_dummies( df, columns = ['Geography'] )

df['AgeBins'] = pd.qcut(df['Age'], q=5)
df = pd.get_dummies( df, columns = ['AgeBins'] )


#df.corr().to_csv(path + "w9c_output.csv")
"""
sign(40)   = 1
sign(0)    = 0
sign(-100) = -1
"""

# DELETE THE COLUMNS WHICH ARE NOT RELATED TO TARGET!!
for c in df.select_dtypes(exclude = ['object']):
	corr = abs(df[c].corr( df['Exited'] ))
	if corr < 0.05:
		del df[c]

for c in ['Age', 'Age_sqrt', 'Age_round', 'Balance', 'Age_pow01', 'Balance_pow01', 'Balance_round', 'Balance_sign']:
	del df[c]

# DELETE THE COLUMNS WHICH ARE RELATED EACHOTHER (VERY HIGH)
for c1 in df.select_dtypes(exclude = ['object']):
	for c2 in df.select_dtypes(exclude=['object']):
		if c1 > c2:
			corr = abs(df[c1].corr(df[c2]))
			if corr > 0.95:
				corr1 = abs( df[c1].corr(df['Exited']) )
				corr2 = abs( df[c2].corr(df['Exited']) )
				print(c1, c2, corr, corr1, corr2)

#: Normally there is no "NULL" but after generated some features, there are some cases, (0 ===> log(0) == nan)

df = df.fillna(0)
df = df.replace([np.inf, -np.inf], 0)




CLFS = [
	RandomForestClassifier(max_depth=6, random_state=0),
	#LinearSVC(),
	#MLPClassifier(max_iter=500, hidden_layer_sizes=(200, 10)),
	BernoulliNB(force_alpha=True),
	KNeighborsClassifier(n_neighbors=3)
]




df.to_csv(path + "w9check.csv")


#: Shuffle
df = df.sample(frac = 1.0)

#: Train/test
limit = int(0.80 * len(df))
train = df[:limit]
test = df[limit:]

trainy = train['Exited']
trainx = train.drop(columns = ['Exited'])

testy = test['Exited']
testx = test.drop(columns = ['Exited'])

print(trainx.shape)

dfresults = {}

for clf in CLFS:
	clf.fit( trainx, trainy )
	result = f1_score( testy, clf.predict( testx ))
	print(clf, result)
	name = str(type(clf))
	name = name.replace("<class '", "")
	name = name.replace("'>", "")
	name = name.split('.')[-1]
	dfresults[ name ] = clf.predict( testx )

dfresults['real'] = testy

dfresults = pd.DataFrame(data = dfresults)

# RandomForestClassifier	BernoulliNB	KNeighborsClassifier

dfresults['sum'] = dfresults['RandomForestClassifier'] + dfresults['BernoulliNB'] + dfresults['KNeighborsClassifier']
dfresults['atleastone'] = dfresults['sum'] > 0
dfresults['all'] = dfresults['sum'] == 3
dfresults['most'] = dfresults['sum'] >= 2
dfresults['avg'] = dfresults['sum'] / 3
# at least one	all	avg	most

print( "f1_score( dfresults['real'], dfresults['most'] )", f1_score( dfresults['real'], dfresults['most'] ) )
print( "f1_score( dfresults['real'], dfresults['all'] )", f1_score( dfresults['real'], dfresults['all'] ) )
print( "f1_score( dfresults['real'], dfresults['atleastone'] )", f1_score( dfresults['real'], dfresults['atleastone'] ) )
# NOTE: IF,



# NOTE: IF THE ACCURACY OR F1 METRIC CHANGES LARGELY, THE DATASET IS NOT BIG ENOUGH

print(dfresults)

dfresults.to_csv( path + "w9voting.csv" )
print(dfresults)
sys.exit(1)
testx['pred'] = clf.predict( testx )
testx['real'] = testy

testx.to_csv(path + "w9anaylsis.csv")
print(result)

