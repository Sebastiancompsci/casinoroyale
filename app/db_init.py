# Database initialization

import sqlite3

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
c.execute("CREATE TABLE teams (id INTEGER PRIMARY KEY, name TEXT, imgUrl TEXT)")

# Create tracked teams table (a user can track one or more teams, so each entry contains a team and a user)
print("Creating tracked_teams table...")
c.execute("CREATE TABLE tracked_teams (id INTEGER PRIMARY KEY, team_id INTEGER, user_id INTEGER)")

# Now insert some dummy data for teams. Use NBA teams for now.
print("Inserting dummy data for teams...")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Atlanta Hawks', 'https://upload.wikimedia.org/wikipedia/en/2/24/Atlanta_Hawks_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Boston Celtics', 'https://upload.wikimedia.org/wikipedia/en/8/8f/Boston_Celtics.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Brooklyn Nets', 'https://upload.wikimedia.org/wikipedia/commons/4/44/Brooklyn_Nets_newlogo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Charlotte Hornets', 'https://upload.wikimedia.org/wikipedia/en/c/c4/Charlotte_Hornets_%282014%29.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Chicago Bulls', 'https://upload.wikimedia.org/wikipedia/en/6/67/Chicago_Bulls_logo.svg')")

# Done
print("Done.")

conn.commit()
conn.close()
