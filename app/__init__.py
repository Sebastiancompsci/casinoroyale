# General imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import requests


# Variables
r = requests.get('https://api.the-odds-api.com')

##with open('nba.txt','w') as fd:
  ##  fd.write(r.content)

# Main route imports
from routes.index import index
from routes.login import login_get, login_post
from routes.register import register_get, register_post
from routes.logout import logout
from routes.odds import odds
from routes.stats import stats
from routes.teams import teams
from routes.about import about
from routes.map import map
from routes.faq import faq

# API route imports
from routes.api.teams import get_tracked_teams, get_teams, set_tracked_teams

app = Flask(__name__)

# Routes
app.add_url_rule('/', 'index', view_func=index)
app.add_url_rule('/login', 'login_get', view_func=login_get, methods=['GET'])
app.add_url_rule('/login', 'login_post', view_func=login_post, methods=['POST'])
app.add_url_rule('/register', 'register_get', view_func=register_get, methods=['GET'])
app.add_url_rule('/register', 'register_post', view_func=register_post, methods=['POST'])
app.add_url_rule('/logout', 'logout', view_func=logout)
app.add_url_rule('/odds', 'odds', view_func=odds)
app.add_url_rule('/stats', 'stats', view_func=stats)
app.add_url_rule('/teams', 'teams', view_func=teams)
app.add_url_rule('/about', 'about', view_func=about)
app.add_url_rule('/map', 'map', view_func=map)
app.add_url_rule('/faq', 'faq', view_func=faq)

# API Routes
app.add_url_rule('/api/profile/tracked_teams', 'get_tracked_teams', view_func=get_tracked_teams, methods=['GET'])
app.add_url_rule('/api/teams', 'get_teams', view_func=get_teams, methods=['GET'])
app.add_url_rule('/api/profile/tracked_teams', 'set_tracked_teams', view_func=set_tracked_teams, methods=['POST'])

# Start
def start():
    # Initialize database
    conn = sqlite3.connect('database.db', check_same_thread=False)
    c = conn.cursor()

    # Add connection to global config
    app.config['conn'] = conn

    # Check if users table exists
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')

    if c.fetchone()[0] == 0:
        # Exit with message
        print('No users table found, did you run db_init.py?')
        exit()

    # Set secret key
    app.secret_key = 'super secret key'
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    start()
