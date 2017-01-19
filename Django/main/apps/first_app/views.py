# this is the controller (views)

from django.shortcuts import render, redirect

def index(request):
  print("*"*10)
  print(request.method+" index method")
  print("*"*10)
  return render(request, "first_app/index.html")

def show(request):
  print("*"*10)
  print(request.method+" show method")
  print("*"*10)
  return render(request, "first_app/show_users.html")

def create(request):
  print (request.method)
  if request.method == 'POST':
    print('*'*50)
    print (request.POST) #case sensitive POST
    print('*'*50)
    request.session['name'] = request.POST['first_name']
    return redirect('/')
  else:
    return redirect('/')