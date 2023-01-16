import sys
import pandas as pd

"""
df = pd.read_csv("/home/mina5/Downloads/datasetA/realtor-data.csv")
df = df.drop_duplicates()
df.to_csv("/home/mina5/Downloads/datasetA/realtor-data-2.csv", index=None)
print(df.shape)
print(df)
"""
"""
Index(['status', 'price', 'bed', 'bath', 'acre_lot', 'full_address', 'street',
       'city', 'state', 'zip_code', 'house_size', 'sold_date'],
      dtype='object')
"""

df = pd.read_csv("/home/mina5/Downloads/datasetA/realtor-data-2.csv")
"""
status           object
price           float64
bed             float64
bath            float64
acre_lot        float64
full_address     object
street           object
city             object
state            object
zip_code        float64
house_size      float64
sold_date        object
dtype: object


"""
import seaborn as sns
import matplotlib.pyplot as plt


df['status'] = df['status'].map({'for_sale': 1, 'ready_to_build': 0})

del df['full_address']
del df['zip_code']
del df['street']

df['city'] = df['city'].map(dict(df.groupby('city').agg({'price': 'mean'}).to_dict())['price'])
df['state'] = df['state'].map(dict(df.groupby('state').agg({'price': 'mean'}).to_dict())['price'])
df['sold_date'] = df['sold_date'].isnull()
df = df.dropna()
q3 = df['price'].quantile(0.99)
df = df[ df['price'] < q3 ]

print(df)

# INDICATOR 1: if data result is different for a given categorical variable, that can be USED to split dataset into two
# NOT YET SPLITTED, BUT IT IS A CANDIDATE TO BE SPLITTED!! MAYBE!!
p1 = df[df['status'] == 0]['price']
p2 = df[df['status'] == 1]['price']
p1 = p1.mean(), p1.std()
p2 = p2.mean(), p2.std()
print(p1, p2)
sys.exit(1)

# INDICATOR 2: DIVIDE BY FILLNESS RATIO
# INDICATOR 3: TRAIN THE MODEL AFTER ANALYZE THE OUTPUT ERROR, THEN DIVIDE ACCORDING TO ERROR'S CORRELATION!!


from sklearn.ensemble import RandomForestRegressor
clf = RandomForestRegressor(max_depth=5, random_state=0)


df = df.sample(frac = 0.5)
print("df.shape", df.shape)
limit = int(0.70 * len(df))
train = df[:limit]
test = df[limit:]
train_y = train['price']
train_x = train.drop(columns = ['price'])

test_y = test['price']
test_x = test.drop(columns = ['price'])
print("training")

clf.fit(train_x, train_y)

test_x['pred'] = clf.predict(test_x)
test_x['real'] = test_y
import numpy as np
test_x['error'] = test_x['pred'] - test_x['real']
test_x['abserror'] = np.abs(test_x['error'])
test_x['mape'] = test_x['abserror'] / ( test_x['pred'] + test_x['real'] )

for c in test_x:
	print(c, test_x[c].corr( test_x['mape'] ))




test_x.to_csv("/home/mina5/Downloads/datasetA/output.csv")



