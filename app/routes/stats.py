# Stats route rule file

from flask import render_template, request, redirect, session
from flask import current_app as app


def stats():
    # If user is logged in
    if 'user' in session:
        # Fetch user data from database by username
        cursor = app.config['conn'].cursor()

        cursor.execute('SELECT * FROM users WHERE username = ?', (session['user'],))
        user = cursor.fetchone()

        # Is none? Redirect to login page
        if not user:
            return redirect('/login')

        # Fetch all tracked teams from database
        cursor.execute('SELECT * FROM tracked_teams WHERE user_id = ?', (user[0],))
        tracked_teams = cursor.fetchall()

        # Render index page with user data and tracked teams
        return render_template('stats.html', user=user[1], tracked_teams=tracked_teams)

    # If user is not logged in
    else:
        # Render index page by default
        return render_template('stats.html')