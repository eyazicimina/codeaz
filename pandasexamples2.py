import sys
import pandas as pd
df = pd.read_csv("Telecom_customer churn.csv", sep = ",")
"""
# dtypes = Types
print(df.dtypes)
for c in df: # for each column in dataframe
	print(c, df.dtypes[c])

# float64        => double
# int64          => long
# datetime64     => datetime
# object         => STRING

# dataframe max is a dictionary of max values for each column
print(df.max().to_dict())
print(df.min())
print(df.mean())




# Transpose
d = df.describe().T
d['Fill Ratio'] = d['count'] / len(df)

# Find the number of "VALUES" (excluding NONES)
# Describe daki, "count" == sum(notnull())
print(sum(df['rev_Mean'].notnull()))

# Find the number of DISTINCT/UNIQUE values
for c in df:
	s = ""
	if df[c].nunique() < 10:
		s = df[c].unique()
	print(c, df.dtypes[c], sum(df['rev_Mean'].notnull()), df[c].nunique(), s)


# The shape of the dataset
print( "df.shape", df.shape )
print( "nof rows", len(df) )

# Shuffle the dataset
df = df.sample( frac = 1.0 )
"""
# Take the first 1000 items
small = df.head(1000)

#: Rasgele 1000 tane row secelim
small = df.sample( n = 1000 )
small = df.sample( frac = 0.05) # Take the %5 of the data (RANDOMLY)


#: Returns the values as "a list of lists"
print(small.values)

#: Print the columns
print("small.columns", small.columns)

#: Copy the dataframe to another dataframe
small2 = small.copy()

print( "small['eqpdays'].count()", small['eqpdays'].count() )

print("small['creditcd'].dtype", small['creditcd'].dtype)

change = {'Y': 1, 'N': 0}
# Change the values
small['creditcd'] = small['creditcd'].replace(change)
print(small)

print("small['Customer_ID'].dtype", small['Customer_ID'].dtype)



