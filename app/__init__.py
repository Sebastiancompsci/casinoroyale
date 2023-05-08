# General imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3

# Route imports
from routes.index import index
from routes.login import login_get, login_post

app = Flask(__name__)

# Routes
app.add_url_rule('/', 'index', view_func=index)
app.add_url_rule('/login', 'login_get', view_func=login_get, methods=['GET'])
app.add_url_rule('/login', 'login_post', view_func=login_post, methods=['POST'])

# Start
def start():
    # Initialize database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Add c to g
    app.config['db'] = c
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run()
