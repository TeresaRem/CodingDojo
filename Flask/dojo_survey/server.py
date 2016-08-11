from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result.html', methods=['POST'])
def result():
	print "Got Post Info"
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('result.html',**locals()) 
	# forgot to change redirect to render_template

@app.route('/hello')
def hello():
	return "hello,world"


app.run(debug=True)