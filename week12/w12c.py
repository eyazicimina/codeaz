import sys
import pandas as pd
df = pd.read_csv("Telecom_customer churn.csv")
df = df.fillna(0)
df = df.select_dtypes(exclude = ['object'])
import random
import warnings
warnings.filterwarnings("ignore")

features = {}
cols = [c for c in df.columns if c != 'churn']
bi_op = ['+',  '*']
mo_op = ['log', 'sqrt']
constant = [0.01, 0.1, 1, 10, 100]
index = 0

desc = {}

import numpy as np
for _ in range(1000):
	m = random.choice( mo_op )
	f = random.choice( cols )
	if m == 'log':
		df['new' + str(index)] = np.log( df[f] )
		desc[ 'new' + str(index) ] = f"np.log( df[{f}] )"
	elif m == 'sqrt':
		df['new' + str(index)] = np.sqrt( df[f] )
		desc['new' + str(index)] = f"np.sqrt( df[{f}] )"
	index += 1

	b = random.choice(bi_op)
	f1 = random.choice( cols )
	f2 = random.choice( cols )

	if b == '+':
		df['new' + str(index)] = df[f1] + df[f2]
		desc['new' + str(index)] = f"df[{f1}] + df[{f2}]"

	elif b == '*':
		df['new' + str(index)] = df[f1] * df[f2]
		desc['new' + str(index)] = f"df[{f1}] * df[{f2}]"
	index += 1



print(df.shape)


for c in df:
	if "new" in c:
		corr = abs(df['churn'].corr( df[c] ))
		if pd.isna(corr):
			del df[c]
		elif corr < 0.10:
			del df[c]
		else:
			print(c, corr, desc[c])

print(df.shape)
sys.exit(1)

new =  list(df.columns)
new = [n for n in new if 'new' in n]

for _ in range(1000):
	m = random.choice( mo_op )
	f = random.choice( new )
	if m == 'log':
		df['new' + str(index)] = np.log( df[f] )
	elif m == 'sqrt':
		df['new' + str(index)] = np.sqrt( df[f] )
	index += 1

	b = random.choice(bi_op)
	f1 = random.choice( new )
	f2 = random.choice( new  )

	if b == '+':
		df['new' + str(index)] = df[f1] + df[f2]
	elif b == '*':
		df['new' + str(index)] = df[f1] * df[f2]
	index += 1


for c in df:
	if "new" in c:
		corr = abs(df['churn'].corr( df[c] ))
		if corr < 0.50:
			del df[c]
		else:
			print(c, corr)

print(df.shape)
