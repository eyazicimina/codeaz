import pandas as pd

df = pd.read_csv("/home/mina5/PycharmProjects/codeaz-python/sales_data_sample.csv")
for datecol in ['ORDERDATE']:
	df[datecol] = pd.to_datetime( df[datecol] )

	# Every year, company grows, customers grow, infulation grow, prices increase
	df['year'] = df[datecol].dt.year     # categoric, numeric
	df['month'] = df[datecol].dt.month   # categoric
	df['day'] = df[datecol].dt.day       # categoric, cok fazla degeri var , 30 tane

	df['weekend'] = df[datecol].dt.dayofweek > 4 # 5. ve 6. gun (saturday, sunday) # FLAG

	df['isSummer'] = (df[datecol].dt.month > 4) & (df[datecol].dt.month < 10) # FLAG

	df['firstDays'] = df['day'] < 5 # FLAG
	df['lastDays'] = df['day'] > 24 # FLAG

#! season
	#! HOLIDAY
	#! Summer break
	#! midterm break
	#! ....
	#! .... [daylength] [evening time - morning time]

	# time related
	# hour
	# minute
	# afternoon
	# day time [morning, noon, afternoon, evening, night]
	# sunset ?
	# sunrise ?
	# working hours
	# lunch time

df.to_csv("w8sample.csv")

# SINGLE VARIABLE FEATURE MINING
# == numeric

#   age ==> log() == nice
#   age ==> sqrt() == nice
#   delete age

# == categoric
#    topN ==> nice
#    targetAverage ==> nice
#    delete ...

# == flag
# == ordinal
# ===> categoric
# ===> numeric


# == ALL
# ===> null or not

c = 'TERRITORY'
df[c] = df[c].isnull()

print(df[c])


# FOR THE SAME VARIABLE WE CAN USE MULTIPLE FEATURE MINING METHODS


