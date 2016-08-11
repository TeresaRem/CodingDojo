from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'very secret'

def random_number():
	session['answer'] = random.randrange(0,101)

@app.route('/')
def index():
	if session['answer'] == '':
		random_number()
		session['correct'] = "none"
		session['high'] = "none"
		session['low'] = "none"
  	return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def user_guess():
  session['guess'] = request.form['guess']
  if int(session['answer']) > int(session['guess']):
  	session['low'] = "block"
  	session['high'] = "none"
  elif int(session['answer']) < int(session['guess']):
  	session['high'] = "block"
  	session['low'] = "none"
  else:
  	session['correct'] = "block"
  	session['low'] = "none"
  	session['high'] = "none"
  print session['answer']
  return redirect('/')

@app.route('/restart', methods = ['POST'])
def check():
	random_number()
	print session['answer']
	session['correct'] = "none"
	session['high'] = "none"
	session['low'] = "none"
	return redirect('/')


if __name__ == "__main__":	# used for importing, instead of executing
    app.run(debug=True)
