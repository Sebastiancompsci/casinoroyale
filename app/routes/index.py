# Homepage route rule file

from flask import render_template, request, redirect

def index():
    return render_template('index.html')
