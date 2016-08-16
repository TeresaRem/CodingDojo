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
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	valid = True
	data = request.form
	if not data['first_name'].isalpha() or len(data['first_name']) < 2:
		error('first_name')
		valid = False
		print "something flashed"
	if not data['last_name'].isalpha() or len(data['last_name']) < 2:
		error('last_name')
		valid = False
	if not EMAIL_REGEX.match(data['email']):
		error('email')
		valid = False
	else:
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
		query = '''INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) 
						VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'''
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
		session['id'] = user[0]['id']
		return redirect('/wall')
	else:
		flash("Login unsuccessful!")
		return redirect('/')

@app.route('/wall')
def wall():
	id = session['id']
	user_query = "SELECT first_name FROM users WHERE id = :id LIMIT 1"
	query_data = {'id' : id }
	user = mysql.query_db(user_query,query_data)
	first_name = user[0]['first_name']

	# query all messages 
	message_query = '''SELECT messages.user_id, messages.id, first_name, last_name, messages.created_at, messages.message 
		FROM users
		JOIN messages ON users.id = messages.user_id
		ORDER BY messages.created_at DESC;'''
	messages = mysql.query_db(message_query)

	# query all comments
	comment_query = '''SELECT first_name, last_name, comments.user_id, comments.id, comments.created_at, comments.comment, message_id
		FROM users
		JOIN comments ON users.id = comments.user_id
		JOIN messages ON messages.id = comments.message_id;'''
	comments = mysql.query_db(comment_query)

	return render_template('wall.html', first_name=first_name, messages=messages,comments=comments)

@app.route('/message', methods=['POST'])
def message():
	# insert message into db
	message = request.form['text']
	if len(message) < 1:
		flash('Please enter a message before posting!')
		return redirect('/wall')
	query = '''INSERT INTO messages (message, created_at, modified_at, user_id) 
					VALUES (:message, NOW(), NOW(), :user_id)'''
	data = {
					'message': message, 
					'user_id': session['id']
					}
	mysql.query_db(query, data)	
	return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
	# THIS DOESNT WORK: YOU NEED TO FIX USER_ID SOMEHOW
	comment = request.form['text']
	if len(comment) < 1:
		flash('Please enter a comment before posting!')
		return redirect('/wall')
	message_id = request.form['message']
	query = '''INSERT INTO comments (message_id, comment, created_at, user_id) 
					VALUES (:message_id, :comment, NOW(), :user_id)'''
	data = {
					'message_id': message_id,
					'comment': comment, 
					'user_id': session['id']
					}
	print data['user_id']
	mysql.query_db(query, data)	
	return redirect('/wall')

@app.route('/logout')
def logout():
	session.clear()
	flash("You have successfully logged out!")
	return redirect('/')

@app.route('/delete_message/<message_id>', methods=['POST'])
def delete_message(message_id):
	# add query for delete messages
	query_comments = '''DELETE comments FROM messages 
										JOIN comments ON messages.id = comments.message_id
										WHERE messages.id = :message_id'''
	query_messages = "DELETE FROM messages WHERE messages.id = :message_id"
	data = {'message_id': message_id}
	mysql.query_db(query_comments, data)	
	mysql.query_db(query_messages, data)	
	return redirect('/wall')

@app.route('/delete_comment/<comment_id>', methods=['POST'])
def delete_comment(comment_id):
	query = "DELETE FROM comments WHERE id = :comment_id"
	data = {'comment_id': comment_id}
	mysql.query_db(query, data)	
	return redirect('/wall')
	
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

app.run(debug=True)