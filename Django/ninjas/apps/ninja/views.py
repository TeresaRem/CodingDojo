from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    "img_url" : "ninja/all.gif"
  }
  return render(request, "ninja/index.html", context)

def color(request,color):
  if color == "orange":
    url = "ninja/orange.jpg"
  elif color == "red":
    url = "ninja/red.jpg"
  elif color == "blue":
    url = "ninja/blue.jpg"
  elif color == "purple":
    url = "ninja/purple.jpg"
  else:
    url = 'ninja/april.gif'
  context = {"img_url": url }
  return render(request, "ninja/index.html", context)