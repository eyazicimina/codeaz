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
	('RF', RandomForestClassifier(max_depth=6, random_state=0)),
	#LinearSVC(),
	#MLPClassifier(max_iter=500, hidden_layer_sizes=(200, 10)),
	('NB', BernoulliNB(force_alpha=True)),
	('KNN', KNeighborsClassifier(n_neighbors=3))
]


#: Shuffle
df = df.sample(frac = 1.0)

#: Train/test
limit = int(0.80 * len(df))
train = df[:limit]

ones = train[ train['Exited'] == 1 ]
zeros = train[ train['Exited'] == 0 ].sample(frac = 0.7)
train = pd.concat( [ ones, zeros ] )

test = df[limit:]

trainy = train['Exited']
trainx = train.drop(columns = ['Exited'])

testy = test['Exited']
testx = test.drop(columns = ['Exited'])

from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import StackingClassifier

cla = VotingClassifier(  estimators=CLFS, voting='hard', weights=(0.45, 0.51, 0.25) )
cla = StackingClassifier( estimators = CLFS, final_estimator=LogisticRegression())
r = cla.fit( trainx, trainy )
print( f1_score(testy, r.predict(testx)) )



# over 0.3 million no meaning!! (rows)
# Accuracy changes %0.001 changes
# deep learning projects
# ALGORTIHMS ARE FOCUSING ON "MOST POPULAR"

# IN MACHINE LEARNING PROJECTS, AT MOST 0.3 should be used
# OR THER ARE TOOOOOOOO MANY COLUMNS


