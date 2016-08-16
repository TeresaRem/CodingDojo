from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'wall')
app.secret_key = 'supersecret'

@app.route('/')
def index():
	session.clear()
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	valid = True
	data = request.form
	if not data['first_name'].isalpha() or len(data['first_name']) < 2:
		error('first_name')
		valid = False
	if not data['last_name'].isalpha() or len(data['last_name']) < 2:
		error('last_name')
		valid = False
	if not EMAIL_REGEX.match(data['email']):
		error('email')
		valid = False
	else:
		# this doesn't work
		user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
		query_data = {'email' : data['email'] }
		user = mysql.query_db(user_query,query_data)
		if user:
			error('email_exists')
			valid = False
	if len(data['password']) < 8:
		error('password')
		valid = False
	if data['password_confirm'] != data['password']:
		error('password_confirm')
		valid = False
	if valid == True:
		flash("You have successfully registered! Please login!")
		password = data['password']
		password = bcrypt.generate_password_hash(password)
		query = '''INSERT INTO users (first_name, last_name, email, password, created_at) 
						VALUES (:first_name, :last_name, :email, :password, NOW())'''
		data = {
						'first_name': data['first_name'], 
						'last_name':  data['last_name'],
						'email': data['email'],
						'password': password
						}
		mysql.query_db(query, data)
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	query_data = {'email' : email }
	user = mysql.query_db(user_query,query_data)
	if bcrypt.check_password_hash(user[0]['password'],password):
		session['id'] = user
		return redirect('/wall')
	else:
		flash("Login unsuccessful!")
		return redirect('/')

@app.route('/wall')
def wall():
	return render_template('wall.html')

@app.route('/logout')
def logout():
	session.clear()
	flash("You have successfully logged out!")
	return redirect('/')

def error(error):
	if error == 'first_name':
		return flash('First name is invalid. Please use only letters with at least two characters.')
	if error == 'last_name':
		return flash('Last name is invalid. Please use only letters with at least two characters.')
	if error == 'email':
		return flash('Email is invalid. Please enter a valid email format.')
	if error == 'password':
		return flash('Password is invalid. Please enter at least eight characters')
	if error == 'password_confirm':
		return flash('Your passwords do not match.')
	if error == 'email_exists':
		return flash('Your email is already in the system. Try an new email address.')

# error('password_confirm')

app.run(debug=True)