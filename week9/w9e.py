import pandas as pd
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
df['odometer'] = df['odometer'].astype(int)
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
df['target'] = df['sellingprice'] - df['mmr']
del df['sellingprice']
del df['mmr']
#: Delete the least important variables
del df['transmission']
################################ Data preparation ################################
#! TODO: transform categorical variables into numerical ones
#! FOR NOW!!!, we only select the numerical ones
df = df.select_dtypes(exclude = ['object', 'datetime'])
print(df.dtypes)

for c in df:
	print(c, df[c].corr(df[target]))


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






