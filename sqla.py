# create a sqlite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if it doesn't exit already
conn = sqlite3.connect("new.db")

# get a cursor object to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
				(city TEXT, state TEXT, population INT )
				""")

# close the database connection
conn.close()

