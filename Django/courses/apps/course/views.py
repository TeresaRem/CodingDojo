from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
  courses = Course.objects.all()
  context = {'courses':courses}
  return render(request,'course/index.html',context)

def add(request):
  if request.method == "POST":
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
  return redirect('/')

def destroy(request, id):
  course = Course.objects.get(id=id)
  context = {'course':course}
  return render(request,'course/delete.html',context)
  pass

def delete(request, id):
  if request.method == "POST":
    print "deleting course with id:",id
    Course.objects.filter(id=id).delete()
  return redirect('/')
