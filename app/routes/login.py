# Login route rule file

from flask import render_template, request, redirect


def login_get():
    return render_template('login.html')

def login_post():
    # Get sqlite cursor from app config
    cursor = request.app.config['db']

    # Get username and password from form
    username = request.form['username']
    password = request.form['password']

    # Attempt to login
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    # If user exists, set session and redirect to home
    if user:
        request.session['user'] = user
        return redirect('/')

    # If user does not exist, we can say the username or password is incorrect
    return render_template('login.html', error='Username or password is incorrect')
