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
# Oh no this is so inefficient.
print("Inserting dummy data for teams...")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Atlanta Hawks', 'https://upload.wikimedia.org/wikipedia/en/2/24/Atlanta_Hawks_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Boston Celtics', 'https://upload.wikimedia.org/wikipedia/en/8/8f/Boston_Celtics.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Brooklyn Nets', 'https://upload.wikimedia.org/wikipedia/commons/4/44/Brooklyn_Nets_newlogo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Charlotte Hornets', 'https://upload.wikimedia.org/wikipedia/en/c/c4/Charlotte_Hornets_%282014%29.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Chicago Bulls', 'https://upload.wikimedia.org/wikipedia/en/6/67/Chicago_Bulls_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Dallas Mavericks', 'https://upload.wikimedia.org/wikipedia/en/9/97/Dallas_Mavericks_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Denver Nuggets', 'https://upload.wikimedia.org/wikipedia/en/7/76/Denver_Nuggets.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Detroit Pistons', 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Pistons_logo17.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Golden State Warriors', 'https://upload.wikimedia.org/wikipedia/en/0/01/Golden_State_Warriors_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Houston Rockets', 'https://upload.wikimedia.org/wikipedia/en/2/28/Houston_Rockets.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Indiana Pacers', 'https://upload.wikimedia.org/wikipedia/en/1/1b/Indiana_Pacers.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Los Angeles Clippers', 'https://upload.wikimedia.org/wikipedia/en/b/bb/Los_Angeles_Clippers_%282015%29.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Los Angeles Lakers', 'https://upload.wikimedia.org/wikipedia/commons/3/3c/Los_Angeles_Lakers_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Memphis Grizzlies', 'https://upload.wikimedia.org/wikipedia/en/f/f1/Memphis_Grizzlies.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Miami Heat', 'https://upload.wikimedia.org/wikipedia/en/f/fb/Miami_Heat_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Milwaukee Bucks', 'https://upload.wikimedia.org/wikipedia/en/4/4a/Milwaukee_Bucks_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Minnesota Timberwolves', 'https://upload.wikimedia.org/wikipedia/en/c/c2/Minnesota_Timberwolves_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('New Orleans Pelicans', 'https://upload.wikimedia.org/wikipedia/en/0/0d/New_Orleans_Pelicans_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('New York Knicks', 'https://upload.wikimedia.org/wikipedia/en/2/25/New_York_Knicks_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Oklahoma City Thunder', 'https://upload.wikimedia.org/wikipedia/en/5/5d/Oklahoma_City_Thunder.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Orlando Magic', 'https://upload.wikimedia.org/wikipedia/en/1/10/Orlando_Magic_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Philadelphia 76ers', 'https://upload.wikimedia.org/wikipedia/en/0/0e/Philadelphia_76ers_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Phoenix Suns', 'https://upload.wikimedia.org/wikipedia/en/d/dc/Phoenix_Suns_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Sacramento Kings', 'https://upload.wikimedia.org/wikipedia/en/c/c7/SacramentoKings.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('San Antonio Spurs', 'https://upload.wikimedia.org/wikipedia/en/a/a2/San_Antonio_Spurs.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Toronto Raptors', 'https://upload.wikimedia.org/wikipedia/en/3/36/Toronto_Raptors_logo.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Utah Jazz', 'https://upload.wikimedia.org/wikipedia/en/0/04/Utah_Jazz_logo_%282016%29.svg')")
c.execute("INSERT INTO teams (name, imgUrl) VALUES ('Washington Wizards', 'https://upload.wikimedia.org/wikipedia/en/0/02/Washington_Wizards_logo.svg')")
print("Done.")

# Done
print("Done.")

conn.commit()
conn.close()
