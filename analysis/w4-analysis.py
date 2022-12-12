#: Imports
import pandas as pd

# PANDAS = EXCEL

df = pd.read_excel("BankChurners.xlsx")
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

# 5- SPLIT


# ---- Standard sapma: cok buyukse, LOG...



