# pandas = excel
import sys
import pandas as pd

#: Read a csv file
# SOMETIMES, when you save it in Excel
# column separator = "sep"
# CSV = Comma(,) separated words
# TSV = Tab separated words sep = "\t"

# Encoding problem - error
# encoding="utf-8"
# encoding="ISO-8859-1"
# encoding="Windows-1254"

# error_bad_lines = False
df = pd.read_csv("small.csv", sep = ",")

# 24,219,22,0,0,0,0,0,0,-157,-19,1,0,1,0,6,0,52,0,42,0,45,0,0,0,0,18,0,91,0,97,0,0,0,0,58,0,133,0,24,0,55,0,1,52,45,0,0,1,61,2,1,U,A,N,1652,4228,1505,1453,4085,1602,30,83,33,272,116,30,322,136,38,S,NORTHWEST/ROCKY MOUNTAIN AREA,Y,N,150,2,2,WCMB,0,0,O,15,S,S,1,M,4,3,C,A,0,N,U,U,U,U,U,Y,361,1000001



# too much detail
# too many sub modules
# too complex

print(df)



# [1424 rows x 100 columns]


excel_way = [['emre', 38, 'male'],        # row 1
	['ahmet', 33, 'male'],       # row 2
	['canan', 23, 'female']      # row 3
] # list of rows
# LIST OF LISTS


# ['emre', 38, 'male']
#  cell1  cell2 cell3

print(excel_way)

excel_way2 = [
	{'name': 'emre', 'age': 38},
	{'name': 'mustafa', 'age': 33},
	{'name': 'canan', 'age': 23},
]
# list of dictionaries

print(excel_way2)


pandas_way = {
	'rev_Mean': [24, 55],
	'mou_Mean': [219, 570],
	'totmrc_Mean': [22, 72]
}

print(pandas_way['rev_Mean'])
print(df['rev_Mean'])

# df yazdiktan sonra yazilan "x" ==> str, kolonu secer
# df[ x ]  (excelde, bir kolona tiklamak gibi)
# df yazdiktan sonra yazilan "x" ==> list[str], kolonlari secer (cogul - plural)
# df[ x ]
# x = ['rev_Mean','mou_Mean']
# df[ x ]
# df yazdiktan sonra yazilan "x" == list[bool], satirlari secer

print("len(df)", len(df))
print("shape", df.shape)
print("columns", df.columns)
print(pandas_way.keys())
# df = dictionary

#: Get the column names in dataframe
for c in df:
	print(c)

# Summary, from the head, from the tail, get the first and last 5 items
print( df.head(5) )
print( df.tail(5) )


ls = ['ahmet', 'mehmet', 'canan', 'mustafa', 'ali']
print(ls[3])
print(df.iloc[3]) # iloc = integer(index) location

print(ls[1:3]) # RANGE
# yatayda, birden fazla satir secme
# selecting multiple rows in given range!!!!
print(df[10:30])

# df['rev_Mean'] ==> pd.Series, numpy array
print( list(df['rev_Mean']) )

# Convert into dictionary
print( df.iloc[10].to_dict() )

# Convert into list of lists
print( df.values )

# ilk 100 kaydi alip baska BIR dataframe'e yazalim
df2 = df.head(100)
df2.to_csv("very_small.csv")

# ========================
# data ==> unique
df = df.drop_duplicates() # overwrite




pandas_way = {
	'rev_Mean': [24, 55],
	'mou_Mean': [219, 570],
	'totmrc_Mean': [22, 72]
}
del pandas_way['rev_Mean']
print(pandas_way)

del df['rev_Mean']
print(df)

# Creating a new column
#! print( df['emre'] )

# a = b
# assign b to a
# a = a
# nothing
#   =  [right side] -- calculate
# [left side] = assign to left side

# READING
df['mou_Mean']
# READING
a = df['mou_Mean']
# READING
print(df['mou_Mean'])
# WRITING
# df['mou_Mean'] = 1


# b = a
# a reading
# b writing

# reading!
#! print( df['emre'] ) # DOES NOT CREATE!!!!!
# writing
df['emre'] = 1 # EVEN IF THERE IS NOT A COLUMN NAMED emre, it automatically CREATES (when writing)
print(df)

df['emre'] = [5 for i in range(len(df))]
print(df)


df['emre'] = [ i for i in range(len(df)) ]
#                                 1425

# df['emre'] = [ i for i in range(len(df)) ]
#                           <---0, 1425-->

df['emre'] = df['mou_Mean'] + df['totmrc_Mean']
df['emre'] = df['mou_Mean'] - df['totmrc_Mean']


print(df)

df['mou_Mean'] + df['totmrc_Mean']

print([5 * i for i in range(len(df))])



df = df.head(5)
#df['mou_Mean'] = [(10, 20), (20, 5), (30, 1), (40, 40), (50, 5)]
#df['totmrc_Mean'] = [[10, 20], [20, 5], [30, 1], [40, 40], [50, 5]]
#print(df)

a = df['mou_Mean'] > 1000 # condition list: LIST OF BOOL
print(a)





print( df[ a ] )



# Select only requested columns
df = df[ ['mou_Mean',  'totmrc_Mean','da_Mean'] ]


# NEW ROW!!!!
# How do we add new row?

# How do we get a row?
print( df.iloc[2] )
# df.iloc[2] XXXX

# df.loc[5] = df.iloc[4]
df.loc[len(df)] = [ 300, 50, 1 ]
df.loc[len(df)] = [ 100, 20, 0 ]
df.loc[len(df)] = [ 90, 30, 2 ]
print(df)

# len(df) = 6
# new index = 6


# 1- mysql den verileri cekip, PANDAS a yazacagiz
# 2- PANDAS dan verileri cekip, mysql'e yazacagiz



import MySQLConnection
query = "Select * from Nefer;"
#result_dataFrame = pd.read_sql(query,MySQLConnection.cnx)
#print(result_dataFrame)


# EMPTY Data Frame -- how to create an empty dataframe
empty = pd.DataFrame( columns = ['id', 'FIN', 'firstname', 'lastname', 'gender', 'birthdate'] )

for record in MySQLConnection.dbSelect("SELECT id, FIN, firstname, lastname, gender, birthdate FROM Nefer LIMIT 5;"):
	# How to add one by one
	empty.loc[len(empty)] = list(record)

print(empty)

#: Loop for each row
for i in range(len(df)):
	#: i th row
	row = list(df.iloc[i].values)
	#MySQLConnection.dbInsert("INSERT INTO ..... (...) VALUES ();")
	print(row.values)

