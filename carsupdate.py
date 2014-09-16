import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory SET quantity = 10 WHERE model = 'Civic'")
	c.execute("UPDATE inventory SET model = 'fairlane' WHERE model = 'mustang'")

	print "\nNew Data:\n"

	c.execute("SELECT * FROM inventory")

	rows = c.fetchall()
	for r in rows:
		print r[0], r[1], r[2]

