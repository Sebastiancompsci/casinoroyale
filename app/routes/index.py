# Homepage route rule file

from flask import render_template, request, redirect, session

def index():
    return render_template('index.html', user=session.get('user'))
