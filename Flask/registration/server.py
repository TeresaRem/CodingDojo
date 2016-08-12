from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['email']) < 1:
		flash("email is required!")
	if len(request.form['first_name']) < 1:
		flash("first name is required!")
	if len(request.form['last_name']) < 1:
		flash("last name is required!")
	if len(request.form['password']) < 1:
		flash("password is required!")
	if len(request.form['confirm_password']) < 1:
		flash("confirm password is required!")
	if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
		flash("name fields cannot contain numbers")
	if len(request.form['password']) < 8:
		flash("password is too short!")
	if not EMAIL_REGEX.match(request.form['email']):
		flash("INVALID EMAIL ADDRESS!")
	if not request.form['password'] == request.form['confirm_password']:
	 	flash("passwords do not match!")
	else:
		flash("success!")
	return redirect('/')

app.run(debug=True)