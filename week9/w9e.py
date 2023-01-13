import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = "/home/mina5/PycharmProjects/codeaz-python/"
df = pd.read_csv(path + "w9car_prices.csv", error_bad_lines=False)
target = 'sellingprice'
# SCORING !!, PRICE ESTIMATION..

"""
from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile.to_file(path + "w9e.html")
"""
"""
print(df['vin'].value_counts())
# wbanv13588cz57827
df[ df['vin'] == 'wbanv13588cz57827' ].to_csv(path + "w9e-problem.csv")
"""


################################ Data preparation ################################
#: Convert to integer
df['odometer'] = df['odometer'].apply( lambda value: int(value / 1000.0) if not pd.isna(value) else None )
df = df[ df['odometer'].notnull() ]
df['odometer'] = df['odometer'].astype(int) + 1.
#df['odometerL'] = np.log(df['odometer'])
#df['odometerP'] = np.power(df['odometer'], 2)
#df['odometerP02'] = np.power(df['odometer'], 0.2)
del df['odometer']

#: Remove some columns
del df['vin']
#: Fill na
df['transmission'] = df['transmission'].fillna('automatic')
#: Transform flag into numeric
df['transmission'] = df['transmission'].map({'automatic': 1, 'manual': 0})
#: Drop na
df = df.dropna()
#: Parse date
# Tue Dec 16 2014 12:30:00 GMT-0800 (PST)
df['saledate'] = df['saledate'].apply(lambda value: " ".join(value.split(" ")[0:4]))
df['saledate'] = pd.to_datetime(df['saledate'], format = "%a %b %d %Y")
#: Remove some makes
df = df[ ~df['make'].isin(['Bentley', 'Aston Martin','Tesla','Ferrari','Geo','Plymouth','Rolls-Royce','Fisker','Lamborghini','Daewoo','Lotus','']) ]
#: Replace with average target variables
data = dict( df.groupby('make').agg({target:'mean'}).to_dict() )['sellingprice']
df['make_average'] = df['make'].map( data )
#: Replace with levels
data = {'Oldsmobile':'very low','Isuzu':'very low','Saturn':'very low','Saab':'very low','Pontiac':'very low','Suzuki':'very low','Mercury':'very low','smart':'very low','Mitsubishi':'low','Volkswagen':'low','Scion':'low','Mazda':'low','FIAT':'low','Buick':'low','Honda':'low','Hyundai':'low','Dodge':'low','Chrysler':'low','Volvo':'low','Nissan':'low','Kia':'low','Chevrolet':'low','Toyota':'low','MINI':'low','Acura':'low','Ford':'low','Jeep':'mid','HUMMER':'mid','Cadillac':'mid','Subaru':'mid','Lincoln':'mid','GMC':'mid','Audi':'mid','Jaguar':'mid','Lexus':'mid','Infiniti':'mid','BMW':'mid','Mercedes-Benz':'mid','Ram':'mid','Land Rover':'very high','Porsche':'very high','Maserati':'very high'}
df['make_levels'] = df['make'].map( data )
#: Replace with average target variables
data = dict( df.groupby('color').agg({target:'mean'}).to_dict() )['sellingprice']
df['color_average'] = df['color'].map( data )
#: Replace yellows with black
df['interior'] = df['interior'].replace('yellow', 'black')
df['interior'] = df['interior'].replace('orange', 'brown')
#: Replace with average target variables
data = dict( df.groupby('interior').agg({target:'mean'}).to_dict() )['sellingprice']
df['interior_average'] = df['interior'].map( data )
#: Change the target
df['target'] = df['sellingprice'] - df['mmr'] # EXPERT ESTIMATION (which is related with "selling price" as 0.98)
# MMR IS ALREADY KNOWN, so it is better to estimate only the "difference"
del df['sellingprice']
del df['mmr']
#: Delete the least important variables
del df['transmission']
"""
#: Create condition variations
df['conditionL'] = np.log(df['condition'])
df['conditionL2'] = np.log2(df['condition'])
df['conditionS'] = np.sqrt(df['condition'])
df['conditionP0.1'] = np.power(df['condition'], 0.1)
df['conditionP2.0'] = np.power(df['condition'], 2.0)
data = df.groupby('condition').agg({'target': 'mean'}).to_dict()['target']
df['condition'] = df['condition'].map(data)
"""
# Working with seller
df['sellerHasBrand'] = df.apply(lambda row: str(row['make']).lower() in row['seller'], axis = 1)
df['isfinancial'] = df['seller'] == 'financial services remarketing (lease)'
df['isca'] = df['state'] == 'ca'
df['isca'] = df['isca'].astype(int)
################################ Data preparation ################################
#! TODO: transform categorical variables into numerical ones
#! FOR NOW!!!, we only select the numerical ones
remaining_cols = df.select_dtypes(include = ['object', 'datetime']).columns
print(remaining_cols)
#df['saleyear'] = df['saledate'].dt.year
#df['salemonth'] = df['saledate'].dt.month
#df['salesummer'] = df['salemonth'].isin( [6,7,8] )
#df['salesummerspring'] = df['salemonth'].isin( [4,5,6,7,8,9,10] )
#df['saleweekend'] = df['saledate'].dt.dayofweek > 4

#! print(remaining_cols)
#! print(df['saledate'].max(), df['saledate'].min())

#! avgs = df.groupby('seller').agg({'target': ['mean', 'count']}).reset_index()
#! avgs.to_csv("avgs.csv")
avgs = pd.read_csv("avgs.csv")
avgs = avgs[ avgs['count'] > 500 ]
avgs = avgs.sort_values(['mean'])
avgs = dict( zip( avgs['seller'], avgs['mean'] ) )
df['seller_value'] = df.apply(lambda row: avgs[ row['seller'] ] if row['seller'] in avgs else 0, axis = 1)

# 500  seller_value 0.2731788199894267
# 1000 seller_value 0.22246277321442137
# 1500 seller_value 0.2159673722390468


"""
words = {}
for i in range(len(df)):
	for word in df.iloc[i]['seller'].split(" "):
		if word not in words:
			words[word] = 0
		words[word] += 1

for w in words:
	print(w, words[w])
"""

df = df.select_dtypes(exclude = ['object', 'datetime'])

for c in df:
	correl = df[c].corr(df['target'])
	if abs(correl) < 0.10:
		print("DELETING", c, correl)
		del df[c]
	else:
		print(c, correl)





#! plt.scatter( df['condition'], df['target'] )
#! plt.show()
# singledata = [2007	bmw	7	series b7 alpina		ca	2.8	97470	black	black	best auto wholesale	18350	17100	1250	Thu Dec 18 2014 12:00:00 GMT-0800 (PST) ]
# clf.predict( [singledata] )[0]
"""
# condition is unknown?

for i in range(1, 6):
	singledata = [2007	bmw	7	series b7 alpina		ca	NULL	97470	black	black	best auto wholesale	18350	17100	1250	Thu Dec 18 2014 12:00:00 GMT-0800 (PST) ]
	singledata[ 7 ] = i
	clf.predict( [singledata] )[0]
"""

from sklearn.ensemble import RandomForestRegressor

regr = RandomForestRegressor(max_depth=5, random_state=0)


from sklearn.linear_model import LinearRegression
#: Shuffle
df = df.sample(frac = 1.0)
#: Normalize
df['condition'] = (df['condition'] - df['condition'].min()) / (df['condition'].max() - df['condition'].min())
df['seller_value'] = (df['seller_value'] - df['seller_value'].min()) / (df['seller_value'].max() - df['seller_value'].min())
df['target'] = (df['target'] - df['target'].min()) / (df['target'].max() - df['target'].min())

#: Limit
limit = int(0.7 * len(df))
train = df[:limit]
test = df[limit:]

trainy = train['target']
trainx = train.drop(columns=['target'])

testy = test['target']
testx = test.drop(columns=['target'])

from sklearn.metrics import r2_score
from sklearn.neural_network import MLPRegressor

da = df.sample(10000)
da['tickness'] = da['target'] + 2
da['tickness'] = da['tickness'] * da['tickness'] * da['tickness']
plt.scatter( da['seller_value'], da['condition'], c=da['tickness'] )
plt.show()

sys.exit(1)
#reg = LinearRegression().fit(trainx, trainy)
reg = MLPRegressor(hidden_layer_sizes=(100,), random_state=1, max_iter=500).fit(trainx, trainy)

print( reg.score( testx, testy ) )

testx['PRED'] = reg.predict(testx)
testx['REAL'] = testy
testx['ERROR'] = testx['PRED'] - testx['REAL']
testx['ABSERROR'] = np.abs( testx['ERROR'] )
testx.to_csv(path + "w9scoring.csv")


# [0.0069862  0.02092187]
# condition       seller_value

# y = 0.27580429279366925 + 0.0069862 * condition + seller_value * 0.02092187



