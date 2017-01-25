from django.shortcuts import render, redirect

from models import User

# Create your views here.
def index(request):
  # User.objects.all().delete()
  users = User.objects.all()
  for user in users:
    print user.email
  if 'messages' in request.session:
    context = {'messages':request.session['messages']}
    del request.session['messages']
  else:
    context = {'messages':[],'users':users}
  return render(request,'login/index.html',context)

def register(request):
  print "register process"
  print request.POST
  if request.method == 'POST':
    messages = User.objects.register(request.POST)
    if not messages:
      print "no messages, success"
      # fetch user id and name via email
      user_list = User.objects.all().filter(email=request.POST['email'])
      request.session['id'] = user_list[0].id
      request.session['name'] = user_list[0].first
      return redirect('/success')
    else:
      request.session['messages'] = messages
  return redirect('/')

def login(request):
  print "login process"
  if request.method == 'POST':
    messages = User.objects.login(request.POST)
    if not messages:
      print "no messages, success"
      # fetch user id and name via email
      user_list = User.objects.all().filter(email=request.POST['email'])
      request.session['id'] = user_list[0].id
      request.session['name'] = user_list[0].first
      return redirect('/success')
    else:
      request.session['messages'] = messages
  return redirect('/')

def success(request):
  name = request.session['name']
  uid = request.session['id']
  context = {"name":name,"id":uid}
  return render(request,'login/success.html',context)

def logout(request):
  if request.method == 'POST':
    del request.session['id']
    del request.session['name']
  return redirect('/')