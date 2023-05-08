# General imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# Route imports
from routes.index import index
from routes.home import home

app = Flask(__name__)

app.add_url_rule('/', 'index', view_func=index)
app.add_url_rule('/home', 'home', view_func=home)

# Start
def start():
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.debug = True
    app.run()
