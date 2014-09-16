# create a sqlite3 database and table

# import the sqlite3 library
import sqlite3

# create a new database if it doesn't exit already
conn = sqlite3.connect("new.db")

# get a cursor object to execute SQL commands
cursor = conn.cursor()

#insert the data
cursor.execute("INSERT INTO population VALUES('NEW YORK CITY', 'NY', 8900000)")
cursor.execute("INSERT INTO population VALUES('SAN FRANSISCO', 'SF', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()

