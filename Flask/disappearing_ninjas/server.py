from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/<color>')
def show_ninja(color):
	if color == "":
		return render_template('ninja.html')
	elif color == 'blue':
		return render_template('ninja.html',color=color)
	elif color == 'red':
		return render_template('ninja.html',color=color)
	elif color == 'purple':
		return render_template('ninja.html',color=color)
	elif color == 'orange':
		return render_template('ninja.html',color=color)
	else:
		return render_template('ninja.html',color='april')


app.run(debug=True)