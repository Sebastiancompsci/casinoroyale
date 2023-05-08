# Odds route rule file

from flask import render_template, request, redirect, session
from flask import current_app as app


def odds():
    # Just render template for now.
    return render_template('odds.html')