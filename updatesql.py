# update and delete statements

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#update data
	c.execute("UPDATE population SET population = 9000000 WHERE city = 'NEW YORK CITY'")

	# update from caps to lower cap
	c.execute("UPDATE population SET city ='New York City' WHERE city = 'NEW YORK CITY'")
	c.execute("UPDATE population SET city = 'San Francisco' WHERE city = 'SAN FRANSISCO'")
	# delete data
	c.execute("DELETE FROM population WHERE city = 'Boston'")

	print "\nNEW DATA:\n"

	c.execute("SELECT * FROM population")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]


