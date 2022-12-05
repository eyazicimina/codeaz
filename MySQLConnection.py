
## SEALED ##

#: Imports
import mysql.connector

#: Create the connection
cnx = mysql.connector.connect(user='sammy2', password='123456', host='127.0.0.1', database='university')

#: Create the cursor
mycursor = cnx.cursor()

# method: rowToDict
# Transforms the sql result row to dictionary
# @row, tuple: The input value tuple
# @names, list: The list of names
# @return, dict: The dictionary
# @completed
def rowToDict( row: tuple, names: list ) -> dict:
	#: Declare variables
	output = {}
	index = 0
	#: Loop for each
	for n in names:
		#: Read the value
		output[n] = row[index]
		index += 1
	#: Return the output
	return output

# method: dbExecute
# Executes a statement
# @sql, str: The execution statement
# @params, tuple: Arguments
# @completed 
# def dbExecute( sql: str, params: tuple ):
# 	mycursor.execute( sql, params )

#* insert
#* delete
#* update
def dbExecute( sql: str):
	mycursor.execute( sql )
	# cnx.commit() # her işlemden sonra gerek yok bir kaç execute sonrası kullanabiliriz en son koy
	
	return int(mycursor.rowcount)
def dbCommit():
	cnx.commit()
	# print(mycursor.rowcount, "record efected.")
	
# method: dbInsert
# Executes an insert statement
# @sql, str: The execution statement
# @params, tuple: Arguments
# @return, int: The row id
# @completed 
def dbInsert(sql):#, params: tuple ) -> int:
	mycursor.execute( sql)#, params )
	return int(mycursor.lastrowid)

# method: dbSelect
# Executes a statement for selecting
# @sql, str: The execution statement
# @params, tuple: Arguments
# @return: Output
# @completed
def dbSelect( sql: str):
	mycursor.execute( sql )
	myresult = mycursor.fetchall()
	return myresult#, [i[0] for i in mycursor.description] <- column names 

