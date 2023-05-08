# Logout route rule file

from flask import render_template, request, redirect, session
from flask import current_app as app


def logout():
    # Delete user from session
    session.pop('user', None)

    # Redirect to login page
    return redirect('/login')
