# this is the controller (views)

from django.shortcuts import render

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
