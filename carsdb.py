import sqlite3

c = sqlite3.connect("cars.db")

cursor = c.cursor()

cursor.execute(""" CREATE TABLE inventory
				(Make TEXT, Model TEXT, Quantity INT)
				""")

c.close()
