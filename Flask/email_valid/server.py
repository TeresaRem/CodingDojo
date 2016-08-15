from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'email')
app.secret_key = 'supersecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/emails',) #
def emails():
	query = "SELECT * FROM email" 
	email = mysql.query_db(query)
	return render_template('success.html', all_emails=email)

@app.route('/success', methods=['POST'])
def success():
	if len(request.form['email']) < 1:
		flash("Email is not valid!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email is not valid!")
	else:
		query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"
		data = {'email':request.form['email']}
		mysql.query_db(query,data)
		flash("The email address you entered ({}) is a VALID email address! Thank you!".format(request.form['email'])) #fix this
		return redirect('/emails')
	return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
	query = "DELETE FROM email WHERE email = :email"
	email = request.form['delete']
	data = {'email': email}
	mysql.query_db(query,data)
	return redirect('/emails')

app.run(debug=True)