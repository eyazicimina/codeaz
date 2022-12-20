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

df = df[ df['STATUS'] == 'Shipped']
print(df['PRODUCTLINE'].value_counts())

#  (Manufaturer suggested retail price)
print(df['MSRP'].describe())


print(df['PRODUCTCODE'].value_counts())
print(df['product number'].value_counts())

print(df['CUSTOMERNAME'].unique())



# ==================================
# print(df.columns)
# print(pd.crosstab(df['COUNTRY'], df['STATUS']))
# print(pd.crosstab(df['COUNTRY'], df['STATUS']).reset_index())
# pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])
# pd.crosstab(df.make, df.body_style, values=df.curb_weight, aggfunc='mean').round(0)
# pd.crosstab(df.make, df.body_style, normalize=True)
# pd.crosstab(df.make, df.body_style, normalize='columns')
# pd.crosstab(df.make, df.body_style, normalize='index')
# grouping: pd.crosstab(df.make, [df.body_style, df.drive_wheels])
# sns.heatmap(pd.crosstab([df.make, df.num_doors], [df.body_style, df.drive_wheels]), cmap="YlGnBu", annot=True, cbar=False)

