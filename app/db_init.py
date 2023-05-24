# Database initialization

import sqlite3
import requests
import os

conn = sqlite3.connect('database.db')

c = conn.cursor()

# State that database is being wiped and reinitialized
print("Wiping database...")
c.execute("DROP TABLE IF EXISTS users")
c.execute("DROP TABLE IF EXISTS teams")
c.execute("DROP TABLE IF EXISTS tracked_teams")

# Create users table
print("Creating users table...")
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

# Create teams table
print("Creating teams table...")
c.execute("CREATE TABLE teams (id INTEGER PRIMARY KEY, name TEXT, imgUrl TEXT, abbreviation TEXT, bgColor TEXT, textColor TEXT)")

# Fetch all teams from our data source
url = "https://wastebin-1-r6722812.deta.app/raw/lcpweixr"
response = requests.get(url)
teams = response.json()

# Insert all teams into database
print("Inserting teams into database...")
for team in teams["teams"]:
    # Note that id is not included, as it is auto-incremented
    c.execute("INSERT INTO teams VALUES (?, ?, ?, ?, ?, ?)", (None, team["name"], team["logo"], team["abbreviation"], team["bgColor"], team["textColor"]))

# Create tracked teams table (a user can track one or more teams, so each entry contains a team and a user)
print("Creating tracked_teams table...")
c.execute("CREATE TABLE tracked_teams (id INTEGER PRIMARY KEY, team_id INTEGER, user_id INTEGER)")

print("Done.")

# Done
print("Done.")

conn.commit()
conn.close()
