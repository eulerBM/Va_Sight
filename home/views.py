from django.shortcuts import render
from home.models import player_key

def home(request):
    objts = player_key.objects.all()

    context = {
        'player': objts,  
                 
    }
    return render (request, 'home.html', context)
