

import pandas as pd

#df = pd.read_csv("xxxx")

def preProcessRow( row: dict ):
	row['Age'] = row['Age'] / 40.0
	row['Salary'] = row['Salary'] / 750.0
	row['Gender'] = 1 if row['Gender'] == 'M' else 0
	return row

# shuffle

# normalize
#df['c'] = (df['c'] - df['c'].min()) / (df['c'].max() - df['c'].min())

# filling
# transformation
# feature selection
# feature engineering
# ...

