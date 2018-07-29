from flask import Flask, render_template
from potato import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login_page():
    return render_template("login.html")