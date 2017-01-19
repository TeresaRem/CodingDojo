# this is the controller (views)
from random import randint
from django.shortcuts import render, redirect

def index(request):
  if not 'count' in request.session:
    request.session['count'] = 1
  print("*"*10)
  print(request.method+" index method")
  print("*"*10)
  return render(request, "rwg/index.html")

def random(request):
  print (request.method)
  if request.method == 'POST':
    request.session['count'] += 1
    # generate 14 random chars
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    string = ""
    for x in range(0,14):
      string += letters[randint(0,len(letters)-1)] 
    request.session['word'] = string
    print('*'*50)
    print(request.session['count'])
    print('*'*50)
    print(request.session['word'])
    print('*'*50)
    return redirect('/')
  else:
    return redirect('/')