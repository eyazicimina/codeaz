import pandas as pd
"""
df = pd.read_excel('Online Retail.xlsx')
#! DO NOT USE THIS df = df.sample( n = 127945 )
# df = df.tail(10000)
# print(df)

invoicelist = list(df['InvoiceNo'].unique())
print(len(invoicelist))
import random
selected_invoice_numbers = random.sample( invoicelist, 1000 )
print(len(selected_invoice_numbers), selected_invoice_numbers)
#: Pick the items whose InvoiceNo is in randomly selected (1000) invoice number
df = df[ df['InvoiceNo'].isin( selected_invoice_numbers ) ]
df.to_csv("Online Retail_1000.csv")
"""

df = pd.read_csv("Online Retail_1000.csv")
#: Delet ethe StockCode, because we do not need to use it, it is same as product description
df = df.drop(columns = ['StockCode'])
# ALTERNATIVE: del df['StockCode']

print(df)

#: Convert to string
df['CustomerID'] = df['CustomerID'].astype(str)
df['CustomerID'] = df['CustomerID'].apply(lambda value: str(value).replace('.0', ''))

#: Create a new column named, TotalPrice
df['TotalPrice'] = df['UnitPrice'] * df['Quantity']

#: Filter out negative quantities
df = df[ df['Quantity'] > 0 ]
df = df[ df['UnitPrice'] > 0 ]

# Parsing a string into datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Customer Value
# Calculate how valuable a customer is

# Data analytics:
# RFM, Popular
# Total Sales Amount [M]onetary
# Total Sales Count [F]requency
# Last Sales Date [R]ecency

# R
# 2011-08-25 A -- RECENT -- yakin zamanda -- we do know about him
# 2010-12-01 B  -- maybe churned? -- maybe dead? -- maybe gets rich -- not enough information

# F (count)
# A 34
# B 1

# M
# A 400
# B 600

import time


# IF, your function is only "ONE" line command, do not need to use "def"
def differenceDays( date ):
	return (pd.Timestamp.now() - date).days

differenceDays3 = lambda date: (pd.Timestamp.now() - date).days
# lambda ==> def

df['DaysPassed'] = df['InvoiceDate'].apply(lambda x: (pd.Timestamp.now() - x).days)
df['DaysPassed2'] = df['InvoiceDate'].apply(differenceDays)
df['DaysPassed3'] = df['InvoiceDate'].apply(differenceDays3)

# ===================================================================
# Frequency
# aggregation: count,
freq = df.groupby(['CustomerID']).count()['InvoiceNo'].reset_index()
freq.columns = [ 'CustomerID', '#invoices' ]
# ===================================================================
# Monetary
# dataframe'i, CustomerID ile GRUPLA !, UnitPrice'in toplamini hesapla
mon = df.groupby(['CustomerID']).agg({'TotalPrice' : 'sum'}).reset_index()
# ===================================================================
# Recency
rec = df.groupby(['CustomerID']).agg({'DaysPassed' : 'min'}).reset_index()

#: Create a dictionary of two columns (key, value)
rec = dict( zip( rec['CustomerID'], rec['DaysPassed'] ) )
mon = dict( zip( mon['CustomerID'], mon['TotalPrice']))
freq = dict( zip( freq['CustomerID'], freq['#invoices']))

#: List the data
for c in rec:
	print(c, rec[c], mon[c], freq[c])

#: Create a new empty dataframe
newEmptyDataFrame = pd.DataFrame(columns = ['CustomerID'])

#: Add new rows
for c in rec:
	newEmptyDataFrame.loc[ len(newEmptyDataFrame) ] = [ c ]

#: LOOKUP = MAP
newEmptyDataFrame['Recency'] = newEmptyDataFrame['CustomerID'].map( rec )
newEmptyDataFrame['Frequency'] = newEmptyDataFrame['CustomerID'].map( freq )
newEmptyDataFrame['Monatery'] = newEmptyDataFrame['CustomerID'].map( mon )

#: Save to file
newEmptyDataFrame.to_csv("rfm.csv")

print(newEmptyDataFrame)

"""
SELECT CustomerID, count(*)
FROM TABLE
GROUP BY CustomerID

SELECT CustomerID, sum(unitprice)
FROM TABLE
GROUP BY CustomerID

"""


# df.groupby(['Name', 'Fruit'])['Number'].agg('sum')
# df.groupby(['Fruit','Name'])['Number'].sum().reset_index()
# df2 = df.groupby('Courses')['Fee'].sum()




