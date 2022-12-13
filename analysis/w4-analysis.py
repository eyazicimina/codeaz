#: Imports
import pandas as pd

# PANDAS = EXCEL

df = pd.read_excel("BankChurners.xlsx")

df = df.rename(columns = {
	'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1': 't1',
	'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2': 't2'
})





print(df['Customer_Age'])
print( "df['Customer_Age'].quantile(0.75)", df['Customer_Age'].quantile(0.75) )

# SCALE
mn = df['Customer_Age'].min()
mx = df['Customer_Age'].max()
rn = mx - mn # RANGE OF THE VALES, FOR EACH COLUMN (NUMERIC) THERE IS A RANGE!!

# Substract minimum from each one
#! df['Customer_Age'] = df['Customer_Age'] - mn
#! df['Customer_Age'] = df['Customer_Age'] / rn
#! print(df['Customer_Age'].describe())

# Single line
#! df['Customer_Age'] = (df['Customer_Age'] - df['Customer_Age'].min()) / (df['Customer_Age'].max() - df['Customer_Age'].min())

#: An alternative approach
#! df['Credit_Limit'] = df['Credit_Limit'] / df['Credit_Limit'].max()

#: An alternative approach
#! df['Credit_Limit'] = df['Credit_Limit'] / df['Credit_Limit'].mean()


# WHY DO WE SCALE?
# 1- COMPARISON: compare visually or verbally
# 2- ALGORITHM:  inputs must be scaled (for some algorithms like neural networks)
# 3- VISUALIZATION: to visualize better
# 4- FEATURE MINING: to sum up or merge them somehow

# ===
# QUARTER = 0.25 demek
q3 = df['Customer_Age'].quantile(0.75)  # 3 tane quarter = 0.75
q1 = df['Customer_Age'].quantile(0.25)  # 1 tane quarter = 0.25
iqr = q3 - q1

upperbound = q3 + 1.5 * iqr  # 1.5 statitically constant
lowerbound = q1 - 1.5 * iqr

print( df[ df['Customer_Age'] >= upperbound ]['Customer_Age'] )

# WHAT DO WE DO WITH OUTLIERS? (cırlaştırma - törpüleme)
# 1- DELETE ROWS?  -- exclude
# df = df[ df['Customer_Age'] <= upperbound ]

# 2- CLIP
# df['Customer_Age'] = df['Customer_Age'].clip( 0, q3 + 1.5 * iqr )
# df['Customer_Age'] = df['Customer_Age'].clip( 0, 65 )

# 3- LEAVE - do not change dataset (rarely used)
# 4- TRANSFORM INTO SOME OTHER SPACE
# log... !! (LATER) -- feature transformation

# 5- SPLIT THE DATASET INTO TWO

# 6- CREATE A NEW COLUMN TO INDICATE THAT IS THE ROW VALUE AN OUTLIER OR NOT


# ---- Standard sapma: cok buyukse, LOG...





for c in df:
	print("CARDINALITY", c, df[c].nunique() / len(df))

#CLIENTNUM
#len(df) =  df[c].nunique()

# CARDINALITY == LOW; categoric or flag variable
# CARDINALITY == HIGH; (1)unique - customer id - customer no, (2)float - 4.545645 almost unique, (3)text -- description, address, phonenumber etc...


"""
statistics = df.describe().T
statistics = statistics.reset_index(names='name')
statistics = statistics.rename( columns= {'name': 'columnname'} )
# for each value (column name), find the df[value].nunique()
statistics['distinct'] = statistics['columnname'].apply( lambda value: df[value].nunique() )
statistics['datatype'] = statistics['columnname'].apply( lambda value: df.dtypes[value] )
statistics['cardinality'] = statistics['distinct'] / statistics['count']
statistics.to_csv("statistics2.csv")
"""

# Limits the dataset by %1!
# We assume that, there are outliers, so we skip the last "%1"
df = df[ df['Credit_Limit'] <= df['Credit_Limit'].quantile(0.99) ]

# .quantile(0.75) = Q3
# .quantile(0.25) = Q1

# Error Analysis, are the causes of "ERRORS" related by outliers

#: Create a column where
# We will use these approach in feature mining section
#! df['Credit_Limit_Outlier1'] = df['Credit_Limit'] > df['Credit_Limit'].quantile(0.75)
#! df['Credit_Limit_Outlier2'] = df['Credit_Limit'] > df['Credit_Limit'].quantile(0.90)
#! df['Credit_Limit_Outlier3'] = df['Credit_Limit'] > df['Credit_Limit'].quantile(0.95)
#!df['Credit_Limit_Outlier'] = df['Credit_Limit_Outlier'].astype(int)
#1print(df.describe())
#!df.to_csv("analysis2.csv")



# MUST CHECK !!!
for i in range(100):
	r = float(i) / 100.0
	print(i, df['Credit_Limit'].quantile(r) )


# Standardization
df['Total_Trans_Amt_STANDARDIZED'] = (df['Total_Trans_Amt'] - df['Total_Trans_Amt'].mean()) / df['Total_Trans_Amt'].std()

print(df['Total_Trans_Amt_STANDARDIZED'].describe())

# Visualization library
import matplotlib.pyplot as plt

"""
for c in df:
	if str(df.dtypes[c]) in ['int64', 'float64']:
		print(c)
		df[c].hist()
		plt.show()
"""
"""

df = pd.read_csv("small.csv")
df = df[ df['totmrc_Mean'] < 150 ]
df = df[ df['da_Mean'] < 56 ]

print(df['change_mou'].describe())
for c in df:
	if str(df.dtypes[c]) in ['int64', 'float64']:
		print(c)
		df[c].hist()
		plt.show()


"""


df = pd.read_csv("small.csv")
df = df[ df['totmrc_Mean'] < 150 ]
df = df[ df['da_Mean'] < 56 ]

print("median", df['numbcars'].median())

# median, sorts the values and picks the item in the MIDDLE
# quantile(0.99) %99 nth items
# median = quantile(0.50) (Q2)

df["mou_Mean"].hist()
plt.show()
df["recv_sms_Mean"].hist()
plt.show()








