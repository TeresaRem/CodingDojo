from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	if len(request.form['name']) < 1:
		flash("Please enter your name!")
		return redirect('/')
	elif len(request.form['comment']) > 120:
		flash("Your comment is too long. Please enter 120 characters or less.")
		return redirect('/')
	else:
		name = request.form['name']
		location = request.form['location']
		language = request.form['language']
		comment = request.form['comment']
		return render_template('result.html',**locals()) 

@app.route('/hello')
def hello():
	return "hello,world"


app.run(debug=True)