from django.shortcuts import render
import datetime 
def index(request):
  print("*"*10)
  print(request.method+" index method")
  print("*"*10)
  # http://strftime.org/
  now = datetime.datetime.now()
  time = {
    "date":now,
    "time":now,
  }
  return render(request, "timedisplay/index.html", time)
