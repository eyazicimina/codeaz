import sys
import numpy as np
import pandas as pd
path = "/home/mina5/Desktop/codeacedemy/"
df = pd.read_csv(path + "week6-quiz1.csv")
df = df.sample(50000)
print(df)

# df = df[(df['Previously_Insured'] == 0) & (df['Vehicle_Damage'] == 'Yes')]

print(df['Response'].mean())

del df['Driving_License']
del df['Gender']
# =============
# Feature representation + Feature mining
#df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Age30'] = df['Age'] > 30
df['Age30'] = df['Age30'].astype(int)

df['Age3059'] = (df['Age'] > 30) & (df['Age'] < 59)

df['Age1'] = df['Age'].isin([84,85,20,82,21,24,25,26,22,23,27,83])
df['Age4'] = df['Age'].isin([32,54,52,51,49,50,42,41,48,39,37,43,40,33,46,44,45,47,34,35,36,38])

values = dict(df.groupby('Age').agg({'Response': 'mean'}))['Response']
df['AgeResponse'] = df['Age'].map(values)

df['Age'] = np.log(df['Age'])
df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes': 1, 'No': 0})




#! df['Vehicle_Age'] = df['Vehicle_Age'].map({'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2})
# NOTE: we can convert into dummies?

#df['myvariable1'] = (df['Previously_Insured'] == 0) & (df['Vehicle_Damage'] == 0)
df['myvariable2'] = (df['Previously_Insured'] == 0) & (df['Vehicle_Damage'] == 1)


df['myvariable5'] = df['Vehicle_Age'].isin(['1-2 Year', '> 2 Years']) & (df['Vehicle_Damage'] == 1) & (df['Previously_Insured'] == 0)
df['myvariable6'] = (df['Vehicle_Age'] == '< 1 Year') & (df['Vehicle_Damage'] == 1) & (df['Previously_Insured'] == 0)
df['myvariable7'] = df['Vehicle_Age'].isin(['1-2 Year', '< 1 Year']) & (df['Vehicle_Damage'] == 0) & (df['Previously_Insured'] == 0)
df['myvariable8'] = df['Vehicle_Age'].isin(['1-2 Year', '< 1 Year']) & (df['Previously_Insured'] == 1)


for c in ['2', '5', '6', '7', '8']:
	df['myvariable' + c] = df['myvariable' + c].astype(int)

df = pd.get_dummies(df, columns = ['Vehicle_Age'])


#df['myvariable3'] = df['Previously_Insured'] + df['Vehicle_Damage']
#df['myvariable4'] = df['Previously_Insured'] * df['Vehicle_Damage']

"""
Region_Code 	Unique code for the region of the customer
Annual_Premium 	The amount customer needs to pay as premium in the year
PolicySalesChannel 	Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.
Vintage 	Number of Days, Customer has been associated with the company (TENURE)
Response 	1 : Customer is interested, 0 : Customer is not interested
"""


df['VintageL'] = np.log(df['Vintage'])
df['VintageS'] = np.sqrt(df['Vintage'])
df['VintageP'] = np.power(df['Vintage'], 2)
df['VintageM'] = df['Vintage'] / 30
df['VintageOM'] = df['Vintage'] > df['Vintage'].mean()
print(df['Vintage'].corr(df['Response']))
print(df['VintageS'].corr(df['Response']))
print(df['VintageOM'].corr(df['Response']))
del df['Vintage']
del df['VintageOM']
del df['VintageM']
del df['VintageP']
del df['VintageS']
del df['VintageL']


# ! Region_Code
# ! Policy_Sales_Channel

print(df['Policy_Sales_Channel'].value_counts())


# HOW DO WE REPRESENT CATEGORICAL VARIABLES
# 1 GET DUMMIES  [list of 1/0]
# 2 DUMMY: SOME OF THEM + OTHER [list of 1/0]
# 3 IS IT MOST? [1/0]
# 4 IS IT IN TOP 5? [1/0]
# 5 GROUPING [ TARGET ] [list of 1/0]
# 6 PROPORTION [float]
# 7 most_important!!! TARGET(avg) [float]

PSC_low = [6,33,34,38,41,46,50,67,70,71,74,75,76,79,82,83,84,95,96,99,102,104,105,112,115,117,118,126,134,137,143,144,146,149,159,160,108,152]
PSC_high = [124,10,94,59,42,44,26,25,57,4,156,136,53,106,150,154,2,68,100,31,157,90,158,80,81,87,101,121,3,163,155,36,27,28,43,123]
PSC_mid = [151,1,18,107,133,98,119,48,63,22,66,64,88,153,132,140,113,65,129,127,73,97,21,8,51,120,19,16,15,135,11,110,130,139,128,32,61,138,37,39,9,14,60,148,93,52,30,20,58,7,131,116,109,125,86,92,103,29,47,78,114,24,145,111,35,40,23,49,89,13,45,55,54,62,69,12,122,91,56,147,17]


PSC = {
	'PSC_low' : [6,33,34,38,41,46,50,67,70,71,74,75,76,79,82,83,84,95,96,99,102,104,105,112,115,117,118,126,134,137,143,144,146,149,159,160,108,152],
	'PSC_high' : [124,10,94,59,42,44,26,25,57,4,156,136,53,106,150,154,2,68,100,31,157,90,158,80,81,87,101,121,3,163,155,36,27,28,43,123],
	'PSC_mid' : [151,1,18,107,133,98,119,48,63,22,66,64,88,153,132,140,113,65,129,127,73,97,21,8,51,120,19,16,15,135,11,110,130,139,128,32,61,138,37,39,9,14,60,148,93,52,30,20,58,7,131,116,109,125,86,92,103,29,47,78,114,24,145,111,35,40,23,49,89,13,45,55,54,62,69,12,122,91,56,147,17]
}

def lookupPSC(value):
	if value in PSC_low: return 'low'
	if value in PSC_mid: return 'mid'
	if value in PSC_high: return 'high'
	return 'unknown'

df['Policy_Sales_Channel'] = df['Policy_Sales_Channel'].apply( lambda value: lookupPSC(value) )
print(df['Policy_Sales_Channel'].value_counts())


# =============================
#: Get the frequencies
rcvals = dict(df['Region_Code'].value_counts())
for c in rcvals:
	rcvals[c] = rcvals[c] / len(df)
#: Get the average respose for each region
rcavgs = dict(df.groupby('Region_Code').agg({'Response': 'mean'}))['Response']
#: Sort by value!
rcavgs = dict(sorted(rcavgs.items(), key=lambda item: item[1]))

da = pd.DataFrame( columns = ['column', 'avgresponse', 'freqratio', 'cummulative_freqratio'] )

cumm = 0
for c in rcavgs:
	cumm += rcvals[c]
	da.loc[ len(da) ] = [c, rcavgs[c], rcvals[c], cumm]

print(da)
da.to_csv(path + "w9_analysis.csv")

def splitDynamically( da: pd.DataFrame, threshold: float = 0.04 ) -> list:
	breakpoints = []
	for i in range(1, len(da)):
		row = da.iloc[i]
		rowM1 = da.iloc[i-1]
		if row['cummulative_freqratio'] - rowM1['cummulative_freqratio'] >= threshold:
			breakpoints.append( row.to_dict()['column'] )
	return breakpoints

breakpoints = splitDynamically( da )
print("breakpoints", breakpoints)

def transformBreakPointsIntoDict( da: pd.DataFrame, breakpoints: list ) -> dict:
	#: Declare variables
	output = {}
	names = ['very low', 'low', 'low mid', 'mid', 'high mid', 'high', 'very high']
	output[ names[0] ] = []

	currentindex = 0
	for i in range(len(da)):
		row = da.iloc[i]['column']
		if currentindex == len(breakpoints):
			break
		if row == breakpoints[currentindex]:
			currentindex += 1
			output[names[currentindex]] = []
		output[names[currentindex]].append( row )

	#: Return
	return output

# [8.0, 46.0, 28.0] # ATTENTION

print(transformBreakPointsIntoDict( da, breakpoints ))

REGION = transformBreakPointsIntoDict( da, breakpoints )

def lookupDict( value ):
	for k in REGION:
		if value in REGION[k]:
			return k
	return 'unknown'

df['Region_Code'] = df['Region_Code'].apply( lambda value: lookupDict( value ))
print(df['Region_Code'].value_counts())


#: Get dummies
df = pd.get_dummies(df, columns= ['Region_Code'])

# Policy_Sales_Channel
dx = dict(df.groupby('Policy_Sales_Channel').agg({'Response': 'mean'})['Response'])

df['Policy_Sales_Channel'] = df['Policy_Sales_Channel'].map( dx )


del df['Annual_Premium']
"""
df['Annual_PremiumL'] = np.log(df['Annual_Premium'])
df['Annual_PremiumS'] = np.sqrt(df['Annual_Premium'])
df['Annual_PremiumP'] = np.power(df['Annual_Premium'], 2)
df['Annual_PremiumOM'] =df['Annual_Premium'] > df['Annual_Premium'].mean()

print(df['Annual_Premium'].corr(df['Response']))
print(df['Annual_PremiumL'].corr(df['Response']))
print(df['Annual_PremiumS'].corr(df['Response']))
print(df['Annual_PremiumP'].corr(df['Response']))
print(df['Annual_PremiumOM'].corr(df['Response']))
"""

# print( df.groupby('Response').agg({'Annual_Premium': 'mean'}) )


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
clf = RandomForestClassifier(max_depth=6, random_state=0) # NORMALDE, 3,4,5,6,7, (do not use 8)
#clf = AdaBoostClassifier(n_estimators=100, random_state=0)

"""
# RE-BALANCE DATASET!!!!!!
ones = df[ df['Response'] == 1 ]
#! zeros = df[ df['Response'] == 0 ].sample(frac = 0.50)
#zeros = df[ df['Response'] == 0 ].sample(frac = 0.40)
zeros = df[ df['Response'] == 0 ].sample(frac = 0.12)
df = pd.concat( [ones, zeros] )
"""
# f1_score 0.6746081504702195
# f1_score 0.7598522167487686
# f1_score 0.8247549019607844



#zeros = df[ df['Response'] == 0 ].sample(frac = 0.20)

#! zeros = df[ df['Response'] == 0 ].sample(frac = 0.60)


y = df['Response']
x = df.drop(columns = ['Response'])
print(x.columns)

"""
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.20)
clf.fit(X_train, y_train)
print( clf.score( X_test, y_test ) )
"""

limit = 0.80
limit = int(len(df) * limit)
train = df[:limit]
test = df[limit:]


train_ones = train[ train['Response'] == 1 ]
train_zeros = train[ train['Response'] == 0 ].sample(frac = 0.15)
train = pd.concat( [train_ones, train_zeros] )

trainy = train['Response']
trainx = train.drop(columns = ['Response'])

testy = test['Response']
testx = test.drop(columns = ['Response'])


clf.fit(trainx, trainy)

importances = clf.feature_importances_
mapper = [(trainx.columns[i], importances[i] ) for i in range(len(trainx.columns))]
for m in mapper:
	print(m)

prob = clf.predict_proba(testx)
testx['pred'] = clf.predict(testx)
testx['prob'] = prob[:,1] #!!!!
testx['real'] = testy
testx['result'] = testx['pred'] == testx['real']

testx['TP'] = testx.apply( lambda row: 1 if (row['pred'] == 1 and row['real'] == 1) else 0, axis = 1 )
testx['TN'] = testx.apply( lambda row: 1 if (row['pred'] == 0 and row['real'] == 0) else 0, axis = 1 )
# Model der ki, "customer" churn edecek (1), ancak gercekte churn etmez (0)
testx['FP'] = testx.apply( lambda row: 1 if (row['pred'] == 1 and row['real'] == 0) else 0, axis = 1 )
testx['FN'] = testx.apply( lambda row: 1 if (row['pred'] == 0 and row['real'] == 1) else 0, axis = 1 )


# TRUE = ACTUAL = REAL
# PRED

from sklearn.metrics import f1_score
print("f1_score", f1_score( testx['real'], testx['pred'] ))

testx[[ 'pred', 'real', 'FP', 'TP', 'FN', 'TN'] ].describe().to_csv(path + "w9_analysis.csv")






trues = testx[ testx['result'] == True ].mean()
falses = testx[ testx['result'] == False ].mean()

print(trues - falses)



testx.to_csv(path + 'w9_output.csv')

"""
Age                     -0.306668
Previously_Insured       0.653427
Vehicle_Damage          -0.695594

Age30                   -0.411207
Age58                   -0.106656
Age3059                 -0.304551
Age34                   -0.402295
Vehicle_Age_1-2 Year    -0.350622
Vehicle_Age_< 1 Year     0.430375
Vehicle_Age_> 2 Years   -0.079753
myvariable1              0.079703
myvariable2             -0.733130
Region_Code_high mid    -0.208000
Region_Code_low          0.016958
Region_Code_low mid      0.030717
Region_Code_mid          0.006503
Region_Code_unknown     -0.000029
Region_Code_very low     0.153851
pred                    -0.809950
real                     0.131899
result                   1.000000
TP                       0.160974
TN                       0.839026
FP                      -0.970925
FN                      -0.029075
dtype: float64
"""

weights = {
	'TP': 200,
	'TN': 5,
	'FP': 45,
	'FN': 200
}

def calculateRealAccuracy( df: pd.DataFrame, weights: dict, threshold: float = 0.50 ) -> float:
	#: Normalize the weights
	weights_sum = np.sum(list(weights.values()))
	for w in weights:
		weights[w] = weights[w] / weights_sum
	#: Calculate the prediction
	df['pred_prob'] = df['prob'] > threshold
	#: Re-calculate the TP, FN ....
	df['TP'] = df.apply( lambda row: 1 if (row['pred_prob'] == 1 and row['real'] == 1) else 0, axis = 1 )
	df['TN'] = df.apply( lambda row: 1 if (row['pred_prob'] == 0 and row['real'] == 0) else 0, axis = 1 )
	df['FP'] = df.apply( lambda row: 1 if (row['pred_prob'] == 1 and row['real'] == 0) else 0, axis = 1 )
	df['FN'] = df.apply( lambda row: 1 if (row['pred_prob'] == 0 and row['real'] == 1) else 0, axis = 1 )

	trues = df['TP'].mean() * weights['TP'] + df['TN'].mean() * weights['TN']
	falses = df['FP'].mean() * weights['FP'] + df['FN'].mean() * weights['FN']

	return trues / (trues + falses)

def findOptimumThreshold( df: pd.DataFrame, weights: dict ):
	max_value = 0
	max_item = None
	for i in [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]:
		r = calculateRealAccuracy( testx, weights, i )
		if r > max_value:
			max_value = r
			max_item = i

	max_value2 = 0
	max_item2 = None
	for i in range(-10, 10):
		newthreshold = max_item + float(i) / 100.0
		r = calculateRealAccuracy( testx, weights, newthreshold )
		if r > max_value2:
			max_value2 = r
			max_item2 = newthreshold

	return max_item2, max_value2


print( findOptimumThreshold(  df, weights ) )








