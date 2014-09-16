import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	carsAdd = [
			('Honda', 'Civic', 2 ),
			('Ford', 'mustang', 1),
			('Ford', 'falcon', 3),
			('Ford', 'ltd', 2),
			('Honda', 'mx', 5)
	]

	c.executemany('INSERT INTO inventory VALUES(?,?,?)', carsAdd)

	