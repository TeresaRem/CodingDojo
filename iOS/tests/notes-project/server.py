from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
from flask_socketio import SocketIO

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'notes')
socketio = SocketIO(app)
app.secret_key = 'supersecret'

if __name__ == '__main__':
    socketio.run(app)

@app.route('/')
def index():
	return render_template('index.html')

# app.run(debug=True)

socketio.run(debug=True)