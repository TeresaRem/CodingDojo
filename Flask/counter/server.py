from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secretness'

def counter():
	session['count'] += 1 

def button():
	session['count'] += 2

@app.route('/')
def index():
	counter()
	return render_template('index.html')

@app.route('/users')
def create_user():
	button()
	print "press"
	return redirect('/')

app.run(debug=True)