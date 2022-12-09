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
# small['creditcd'] = small['creditcd'].replace(change)
small['creditcd'] = small['creditcd'].map(change)
print(small)

print("small['Customer_ID'].dtype", small['Customer_ID'].dtype)

# Change the type of the column to string
small['Customer_ID'] = small['Customer_ID'].astype(str)
# Change the type of the column to float
small['comp_vce_Mean'] = small['comp_vce_Mean'].astype(float)

print(small.dtypes['Customer_ID'])
print(small.dtypes['comp_vce_Mean'])

# Registration plate code, 99 = Baku, STRING, no mathematical operation can be performed!


# Filtering the dataset
# dwlltype = 'M'

# df[]
# str ==>   column selection
# range ==> subset
# list<str> ==> columns
# list<bool> ==> filter

small[ ['Customer_ID', 'comp_vce_Mean'] ]

#: Subset selection
small3 = small[100:500] # list


#: Filter the dataset
subset1 = small[ small['dwlltype'] == 'M' ]
subset2 = small[ small['dwlltype'] != 'M' ]
print(subset1.shape, subset2.shape, small.shape)


# BUYUK EV SAHIBI OLANLAR (medium size, house owners)
subset3 = small[ (small['dwlltype'] == 'M') & (small['ownrent'] == 'O') ] # and
subset4 = small[ (small['dwlltype'] == 'M') | (small['ownrent'] == 'O') ] # or
print(subset4)


# small.sample(n = 1000)
# Data balancing

# (numbcars == 3) %50
# rest            %100

threecars = small[ small['numbcars'] == 3 ]
notthreecars = small[ small['numbcars'] != 3 ]
print(threecars.shape)

#threecars = threecars.sample(frac = 0.50)
threecars = threecars[0: int(len(threecars) / 2)]

concated = pd.concat( [threecars, notthreecars] )
print(concated)


columnstopick = ['creditcd', 'eqpdays','Customer_ID']
columnstopick2 = [i for i in small.columns if i not in columnstopick]
print(columnstopick2)

# METHOD 1
rightside = small[ columnstopick ]
leftside = small[ columnstopick2 ]

# METHOD 2
rightside = small[ columnstopick ]
leftside = small.drop( columns = columnstopick)
print(leftside)

# SELECT * FROM TABLE WHERE <..condition...>
subset4 = small.query("dwllsize == 'J'")
subset5 = small[ small['dwllsize'] == 'J' ]
print(subset4.shape)
print(subset5.shape)

#: Create a new column, sum of two other
small['new'] = small['rev_Mean'] + small['mou_Mean']
print( small[['new','rev_Mean','mou_Mean']] )

# apply = for each!
small['area'] = small['area'].apply( lambda value: str(value).replace(' AREA', '')  )

small['rich1'] = small['numbcars'].apply( lambda value: 1 if value > 2 else 0 )
small['rich2'] = small['numbcars'] > 2

# True false ==> 1/0 a nasil ceviririz?
small['rich2'] = small['rich2'].astype(int)

print(small[['numbcars', 'rich1', 'rich2']])





import re
def isWest2( text: str ) -> bool:
	if re.match(".*WEST.*", text):
		return True
	return False



def isWest( text: str ) -> bool:
	return "WEST" in text

small['isWest'] = small['area'].apply( isWest ) # apply is calling the parameter function, for each value


# x < 50:  S
# x < 100: M
# else   : L
print(small[ ['isWest', 'area'] ])

def level( x: int ) -> str:
	if x < 50: return 'S'
	elif x < 100: return 'M'
	else: return 'L'

small['levels'] = small['avg6rev'].apply(level)
print(small[ ['levels', 'avg6rev'] ])


