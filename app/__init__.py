# Init.py for Flask App

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

# Start
def start():
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.route("/home")
def homepage():
    return render_template("home.html")

if __name__ == '__main__':
    app.debug = True
    app.run()