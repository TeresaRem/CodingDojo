from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secretness'

def counter():
	session['count'] += 1 

@app.route('/')
def index():
	if "count" not in session:
		session['count'] = 1
	else:
		counter()
	return render_template('index.html')

@app.route('/users')
def create_user():
	counter()
	print "press"
	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)