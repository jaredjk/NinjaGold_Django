from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# Create your views here.
def index(request):
    if not 'gold' in request.session: 
        request.session['gold'] = 0 #having 'gold' start from 0
    if not 'messages' in request.session:
            request.session['messages'] = [] # having message starting from empty brackets
    return render(request, 'goldnin/index.html')

def process(request):
    if request.method == "POST": 
        if request.POST['place'] == 'farm': 
            temp_gold = random.randrange(10,21)
            request.session['gold'] += temp_gold
        if request.POST['place'] == 'cave':
            temp_gold = random.randrange(5,11)
            request.session['gold'] += temp_gold
        if request.POST['place'] == 'house':
            temp_gold = random.randrange(2,6)
            request.session['gold'] += temp_gold
        if request.POST['place'] == 'casino':
            temp_gold = random.randrange(-50,50)
            request.session['gold'] += temp_gold
        if request.POST['place'] == 'reset':
            request.session['gold'] = 0
            request.session['messages'] = []
            return redirect('/')
        if temp_gold > 0:
            earn_lost = 'positive'
        else:
            earn_lost = 'negative'
        temp_message = {'gold':temp_gold,'place':request.POST['place'],'earn_lost':earn_lost, 'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())}
        request.session['messages'].append(temp_message)
    return redirect('/')