# Teams route rule file

from flask import render_template, request, redirect, session
from flask import current_app as app


def teams():
    # Just render template for now.
    return render_template('teams.html')