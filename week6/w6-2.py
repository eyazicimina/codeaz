import pandas as pd
df = pd.read_csv("sales_data_sample.csv", encoding='latin-1', error_bad_lines=False)


import numpy as np
from numpy.linalg import norm

# sub module
# numpy = top module
#         linalg (linear algorithms) = sub module
#         folder like!!

# define two lists or array
A = np.array([2,1,2,3,1,9])
B = np.array([2,1,2,3,5,9])

# Cosine similarity == [0, 1] == 1 identical, high = very similar, 0 not similar

# compute cosine similarity
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity:", cosine)

# EVERY DISTANCE METRIC become useless when there is a high dimensional data
# 30 dimension ==> euclidean = KOTU = BAD RESULTS
#              ==> cosine (better)

# SPARSE DATA
# cosine better
# euclidean bad

# distribution ==> cok farkliysa, ikisi icinde problem (ama euclidean icin daha problem)



# ---------------------------------
# VERI TEMIZLEME
# DATA PURIFICATION
# <DROP SOME ROWS BY>:
#    - invalid value
#    - data problem, typo, not consistent value
#    - [LAWYER], [HIGH SCHOOL LISE MEZUNU]
#    - [HANIM],  [ASKERLIK = YAPMISTIR]
#    - [17 YAS], [EVLIDIR]
#    - [...]
#    - YAS: 435 [devletten web service, ..query]
#    - YAS: -12
#    - LIMIT, INVALID

# To overcome these problems:
#  -- EXCLUDE
#  -- FIX, CORRECT

# Get the difference between this value and previous ROW
df['SIRA-FARKI'] = df['ORDERNUMBER'] - df['ORDERNUMBER'].shift(1)
print(df['SIRA-FARKI'])

print(df['PRICEEACH'].describe())

df['PRICEEACH'] = df['PRICEEACH'].clip(0, 100)
df['PRICEEACH'] = df['PRICEEACH'].apply( lambda value: 100 if value > 100 else value )

dfA = df[   df['PRICEEACH'] > 99 ]
dfB = df[   df['PRICEEACH'] <= 99 ]


print( df['ORDERLINENUMBER'].describe() )
print(df['ORDERLINENUMBER'].value_counts())
# print(df['ORDERNUMBER'].nunique())

max_values = df.groupby(['ORDERNUMBER']).agg({'ORDERLINENUMBER': 'max'}).reset_index()

print("============================================")
#print( max_values['ORDERLINENUMBER'].value_counts() )
import matplotlib.pyplot as plt
# plt.hist(max_values['ORDERLINENUMBER'])
# plt.show()

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
print(df['ORDERDATE'].value_counts())

# 29 months

print(df['STATUS'].value_counts())

# CUSTOMER VALUE
# R(F)M, satis adedi = count = frequency

#df = df[ df['STATUS'] == 'Shipped']
print(df['PRODUCTLINE'].value_counts())

#  (Manufaturer suggested retail price)
print(df['MSRP'].describe())


print(df['PRODUCTCODE'].value_counts())
print(df['product number'].value_counts())

print(df['CUSTOMERNAME'].unique())

#: Set the maximum width of a table to be shown as "100"
pd.set_option('display.max_columns', 100)

# Creating an empty dataframe
dx = pd.DataFrame(columns = ['a', 'b', 'c'])
# Creating a data frame from a given list of lists!
l = [
	[1,2,'q'],
	[4,5,'p'],
	[7,8,'z']
]
#dx = pd.DataFrame(l, columns = ['a', 'b', 'c'])
# read_csv ....
# sum( [1,2,3] ) ==> 6


num_df = df.select_dtypes(include=np.number)
# type(..) is int









# ==================================
print(df.columns)
print(pd.crosstab(df['COUNTRY'], df['STATUS']))
pd.crosstab(df['COUNTRY'], df['DEALSIZE']).to_csv("w6_crosstab.csv")
#dx = pd.read_csv("Telecom_customer churn.csv")
#pd.crosstab(dx['ownrent'], dx['dwlltype']).to_csv("w6_crosstab.csv")

print(pd.crosstab(df['COUNTRY'], df['STATUS']).reset_index())
#pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])


"""
SELECT COUNTRY, STATUS, count(*)
FROM TABLE
GROUP BY COUNTRY, STATUS
"""



"""
SELECT COUNTRY, STATUS, AVG(SALES)
FROM TABLE
GROUP BY COUNTRY, STATUS
"""

pd.crosstab(df['COUNTRY'], df['DEALSIZE'], values=df.SALES, aggfunc='mean', normalize='index').to_csv("w6_crosstab.csv")


#.round(0)
# pd.crosstab(df.make, df.body_style, normalize=True)
# pd.crosstab(df.make, df.body_style, normalize='columns')
# pd.crosstab(df.make, df.body_style, normalize='index')
# grouping: pd.crosstab(df.make, [df.body_style, df.drive_wheels])

dq = pd.crosstab(df['COUNTRY'], [df['DEALSIZE'], df['STATUS']])
dq = dq.reset_index()
#dq.columns = [i for i in range(18)]
#pd.crosstab(df['COUNTRY'], [df['DEALSIZE'], df['STATUS']]).to_csv("w6_crosstab.csv")
dq = pd.DataFrame(dq)
dq = dq.reset_index()
print(dq.iloc[0])
print(dq.iloc[1])
print(dq.columns)

dq.columns = [  i[0] + '-' + i[1] for i in dq.columns]

dq.to_csv("w6_crosstab.csv")

import seaborn as sns
sns.heatmap(pd.crosstab(df['COUNTRY'], df['DEALSIZE']), cmap="YlGnBu", annot=True, cbar=True)
plt.show()


