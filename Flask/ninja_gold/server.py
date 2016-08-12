from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = 'very secret'

def farm():
  g = random.randrange(10,21)
  session['gold'] += g
  session['messages'].insert(0,'Earned {} gold from the farm! ({})'.format(g,datetime.datetime.now()))

def cave():
  g = random.randrange(5,11)
  session['gold'] += g
  session['messages'].insert(0,'Earned {} gold from the cave! ({})'.format(g,datetime.datetime.now()))

def house():
  g = random.randrange(2,6)
  session['gold'] += g
  session['messages'].insert(0,'Earned {} gold from the house! ({})'.format(g,datetime.datetime.now()))

def casino():
  g = random.randrange(-50,51)
  session['gold'] += g
  if g < 0:
    session['messages'].insert(0,'Entered a casino and lost {} gold... Ouch! ({})'.format(abs(g),datetime.datetime.now()))
    session['win_lose_color'] = 'red'    
  else:
    session['messages'].insert(0,'Entered a casino and won {} gold!!! ({})'.format(g,datetime.datetime.now()))
    session['win_lose_color'] = 'green'    

def time_now():
  d = datetime.datetime.now()
  # format = '%Y-%m-%d %H:%M %p'
  # d = datetime.datetime.strptime(d, format)
  return d

@app.route('/')
def index():
  if 'gold' not in session:
    session['gold'] = 0
  if 'messages' not in session:
    session['messages'] = []

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
    
  return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
  session.clear()
  session['gold'] = 0

  return redirect('/')


if __name__ == "__main__":  # used for importing, instead of executing
    app.run(debug=True)
