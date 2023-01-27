#: Imports
import time

lastId = 0

#: Infinite loop
while True:
	#: Fetch new records
	sql = f"SELECT * FROM CUSTOMERS WHERE CustomerID > {lastId}"
	for r in fetch(sql):
		#
		preprocess
		prediction
		#
		lastId = r['CustomerId']

	#: For each 10 minutes
	time.sleep(10 * 60)