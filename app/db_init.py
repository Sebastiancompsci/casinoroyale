# Database initialization

import sqlite3

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

# State that database is being wiped and reinitialized
print("Wiping database...")
c.execute("DROP TABLE IF EXISTS users")

# Create users table
print("Creating users table...")
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

# Done
print("Done.")

conn.commit()
conn.close()
