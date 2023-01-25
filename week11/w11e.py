import math
import numpy as np
import pandas as pd
df = pd.read_csv("Telecom_customer churn.csv")

df = df.sample(frac = 1.0)

for _ in range(10):
	y = df.sample(n = 11) # take 11 random records
	x = y.mean().to_dict() # find the mean!
	for c in df.select_dtypes(include = ['object']).columns: # for the categoric variables
		x[ c ] = y[c].mode()[0] # find the mode
	print(x)


for value in df[ df['marital'].notnull() ]['marital'].unique():
	for _ in range(10):
		y = df[ df['marital'] == value ].sample(n = 11) # take 11 random records
		x = y.mean().to_dict() # find the mean!
		for c in df.select_dtypes(include = ['object']).columns: # for the categoric variables
			x[ c ] = y[c].mode()[0] # find the mode
		x[ 'marital' ] = value



counts = df['churn'].value_counts().to_dict()
for c in counts:
	counts[c] = int(100 * counts[c] / len(df)) # balance

for c in counts: # {0: 50, 1: 49}
	for i in range(counts[c]):
		y = df[ df['churn'] == c ].sample(n = 11) # take 11 random records
		x = y.mean().to_dict() # find the mean!
		for c in df.select_dtypes(include = ['object']).columns: # for the categoric variables
			x[ c ] = y[c].mode()[0] # find the mode
		print(x)
