from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'very secret'

def farm():
  session['gold'] += random.randrange(10,21)

def cave():
  session['gold'] += random.randrange(5,11)

def house():
  session['gold'] += random.randrange(2,6)

def casino():
  session['gold'] += random.randrange(-50,51)

@app.route('/')
def index():
  if session['gold'] != ''
    session['gold'] = 0

  return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
  
  session['building'] = request.form['building']
  print session['building']

  if session['building'] == 'farm':
    farm()
  elif session['building'] == 'cave':
    cave()
  elif session['building'] == 'house':
    house()
  else:
    casino()

  print session['gold']
  return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
  session.clear()
  session['gold'] = 0

  return redirect('/')


if __name__ == "__main__":  # used for importing, instead of executing
    app.run(debug=True)
