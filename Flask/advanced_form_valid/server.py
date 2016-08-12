from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("INVALID EMAIL ADDRESS!")
	else:
		flash("success!")
	return redirect('/')

app.run(debug=True)