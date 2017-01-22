from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
  if not 'gold' in request.session:
    request.session['gold'] = 0
  if not 'message' in request.session:
    request.session['message'] = []
  return render(request, 'gold/index.html')

def process(request):
  if request.POST['building'] == "farm":
    more_gold = random.randint(10, 20)
    request.session['message'].append("Earned {} gold from the farm!".format(more_gold)) 
    request.session['gold'] += more_gold
  elif request.POST['building'] == "cave":
    more_gold = random.randint(5, 10)
    request.session['message'].append("Earned {} gold from the cave!".format(more_gold)) 
    request.session['gold'] += more_gold
  elif request.POST['building'] == "house":
    more_gold = random.randint(2, 5)
    request.session['message'].append("Earned {} gold from the house!".format(more_gold)) 
    request.session['gold'] += more_gold
  else:
    #casino
    more_gold = random.randint(-50, 50)
    if more_gold > 0:
      request.session['message'].append("Earned {} gold from the casino!".format(more_gold)) 
    else:
      request.session['message'].append("Lost {} gold from the casino! :(".format(more_gold)) 
    request.session['gold'] += more_gold
  return redirect('/')