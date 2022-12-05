
import MySQLConnection
rows = MySQLConnection.dbSelect("select userid, Score from user_scores limit 10;")

for row in rows:
	print(row)



