# Login route rule file

from flask import render_template, request, redirect, session
from flask import current_app as app


def login_get():
    return render_template('login.html')

def login_post():
    # Get sqlite cursor from app config
    cursor = app.config['conn'].cursor()

    # Get username and password from form
    username = request.form['username']
    password = request.form['password']

    # Attempt to login
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    # Close cursor
    cursor.close()

    # If user exists, set session and redirect to home
    if user:
        session['user'] = user[1]
        return redirect('/')

    # If user does not exist, we can say the username or password is incorrect
    return render_template('login.html', error='Username or password is incorrect')
