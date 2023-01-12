import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# THE MOST IMPORTANT TOPIC
# 1- Feature Representation, Evaluation
# 2- Feature Extraction & Feature Mining
# 3- Feature Selection [criteria]

# FEATURE = COLUMN = ATTRIBUTE = SUTUN = KOLON

# How do we represent the features
df = pd.read_csv("/home/mina5/Desktop/codeacedemy/week6-quiz1.csv")
# ===========================================================================
#### NUMERIC
## AS IS ==> oldugu gibi
#! df['Age'] = df['Age']
## AS Normalized
df['AgeN'] = (df['Age'] - df['Age'].min()) / ( df['Age'].max() - df['Age'].min() )
## AS Standardized
df['AgeS'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()
## AS 10's
# TORPULEME, (round(72, -1) = 70)
df['AgeT'] = df['Age'].round(-1) / 10
df['AgeT'] = df['AgeT'].astype(int)

# 5'li
# ?( 44 ) ==> 45
# ?( 31 ) ==> 30

def yuvarla5( value: int ) -> int:
	remaining = value - value % 5 # ==> 79, 4 ==> 79-4 = 75
	if value % 5 > 2:
		remaining += 5
	return remaining

def yuvarla5_Alternative(num):
	return np.round(num/5) *5

df['AgeR'] = df['Age'].apply(yuvarla5)

# round(3.5) ==> 4
# round(3.123, 1) = 3.1
# round(3.123, 2) = 3.12
# round(3.123, 3) = 3.123
# round(51) = 50

## AS LEVELS
df['AgeL'] = pd.qcut(df['Age'], q=[0,0.2,0.4,0.6,0.8,1], labels=False)

## FUNCTION
df['AgeF1'] = np.log( df['Age'] )
df['AgeF2'] = np.sqrt( df['Age'] )
df['AgeF3'] = np.power( df['Age'], 2 )
df['AgeF4'] = np.power( df['Age'], 0.1 )
df['AgeF5'] = np.power( df['Age'], 0.7 )
df['AgeF6'] = np.power( df['Age'], 1.5 )

# square root (power(x, 0.5))

df['Age>1'] = df['Age'] > df['Age'].mean()    # True/False
df['Age>2'] = df['Age'] > df['Age'].median()  # True/False
df['Age>3'] = df['Age'] > (df['Age'].mean() - df['Age'].std())
df['Age>4'] = df['Age'] > df['Age'].quantile(0.40)
df['Age>5'] = df['Age'] > 30
df['AgeSign'] = np.sign(df['Age']) # Bank, Customer Balance (negatif, pozitif)
df['Age2N'] = np.power(2, df['Age'])
df['AgeL2'] = np.log2(df['Age'])

def sigmoid(x):
	y = (x - x.min()) / (x.max() - x.min())
	return 1/(1 + np.exp(-y))

df['AgeSigmoid'] = sigmoid(df['Age'])

"""
if variation == "rank": return rankdata(self.dataFrame[column])
if variation == "sigmoid": return sigmoid(self.dataFrame[column])
if variation == "valueOverMean": return self.dataFrame[column] / self.dataFrame[column].mean()
if variation == "valueMinusMean": return self.dataFrame[column] - self.dataFrame[column].mean()
if variation == "tanh": return np.tanh(self.dataFrame[column])
if variation == "arctan": return np.arctan(self.dataFrame[column])
if variation == "gaussian": return gaussian(self.dataFrame[column])
if variation == "valueMinusMeanOverStd": return (self.dataFrame[column] - self.dataFrame[column].mean()) / \
																								self.dataFrame[column].std()
if variation == "valueMinMax": return (self.dataFrame[column] - self.dataFrame[column].min()) / (
					self.dataFrame[column].max() - self.dataFrame[column].min())
"""







# print(df['Age'].describe(percentiles=[0.40,0.45]))
# df['Annual_Premium'].plot(kind='hist')
# plt.show()





age_columns = [c for c in df.columns if c.startswith('Age') or c == 'Response']
sub = df[age_columns]

for c in sub:
	print(c, sub[c].corr(sub['Response']))
sub.to_csv("w7_sub.csv")





# ===========================================================================

# ===========================================================================

"""
def bizimMahalanobis( a: pd.Series, b: pd.Series ) -> float:

	for i in range(len(xx)):
		total += math.pow(a[i] - b[i], 2) / std[i] # more simple!!

	return math.squrt(total)
"""



