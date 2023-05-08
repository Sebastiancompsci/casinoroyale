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

# Create teams table
print("Creating teams table...")
c.execute("CREATE TABLE teams (id INTEGER PRIMARY KEY, name TEXT)")

# Create tracked teams table (a user can track one or more teams, so each entry contains a team and a user)
print("Creating tracked_teams table...")
c.execute("CREATE TABLE tracked_teams (id INTEGER PRIMARY KEY, team_id INTEGER, user_id INTEGER)")

# Done
print("Done.")

conn.commit()
conn.close()
