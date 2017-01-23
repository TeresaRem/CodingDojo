from django.shortcuts import render, redirect
from .models import Email
# Create your views here.
def index(request):
  return render(request,'email_/index.html')

def process(request):
  # NEED TO USE MESSAGES (FLASH) INSTEAD OF SESSION
  if request.method == 'POST':
    valid = Email.objects.test(request.POST)
    if valid == True:
      request.session['message'] = "The email address you entered {} is a VALID email address! Thank you!".format(request.POST['email'])
      return redirect('/success')
    else:
      request.session['message'] = valid
      return redirect('/')
  return redirect('/')

def success(request):
  emails = Email.objects.all()
  context = {'emails':emails}
  return render(request,'email_/success.html',context)

def delete(request, id):
  if request.method == 'POST':
    Email.objects.filter(id=id).delete()
    return redirect('/success')
  return redirect('/success')