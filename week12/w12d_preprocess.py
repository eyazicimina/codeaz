import pandas as pd
path = "/home/mina5/PycharmProjects/codeaz-python/w12/week6-quiz1.csv"
df = pd.read_csv(path)
ageMIN = df['Age'].min()
ageMAX = df['Age'].max()

import json
import os

if not os.path.isfile("constants.json"):
	json.dump({'ageMIN': float(ageMIN), 'ageMAX': float(ageMAX)}, open('constants.json', 'w'))

data = json.load(open('constants.json'))
ageMAX = data['ageMAX']
ageMIN = data['ageMIN']

def prepareRow( row ):
	def VehicleAgeMap(value: str) -> int:
		if value == '< 1 Year': return 0
		if value == '1-2 Year': return 1
		return 2

	row['Age'] = (row['Age'] - ageMIN) / (ageMAX - ageMIN)
	row['Gender'] = 1 if row['Gender'] == 'Male' else 0
	row['Vehicle_Damage'] = 1 if row['Vehicle_Damage'] == 'Yes' else 0
	row['Vehicle_Age'] = VehicleAgeMap( row['Vehicle_Age'] )

	return row

