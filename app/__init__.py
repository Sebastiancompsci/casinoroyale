# General imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3

# Route imports
from routes.index import index
from routes.login import login_get, login_post
from routes.register import register_get, register_post
from routes.logout import logout

app = Flask(__name__)

# Routes
app.add_url_rule('/', 'index', view_func=index)
app.add_url_rule('/login', 'login_get', view_func=login_get, methods=['GET'])
app.add_url_rule('/login', 'login_post', view_func=login_post, methods=['POST'])
app.add_url_rule('/register', 'register_get', view_func=register_get, methods=['GET'])
app.add_url_rule('/register', 'register_post', view_func=register_post, methods=['POST'])
app.add_url_rule('/logout', 'logout', view_func=logout)

# Start
def start():
    # Initialize database
    conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
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
