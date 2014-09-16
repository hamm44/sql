import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT * from inventory")
	rows = c.fetchall()

	for r in rows:
		if r[0] == 'Ford':
			print r[0], r[1], r[2]
