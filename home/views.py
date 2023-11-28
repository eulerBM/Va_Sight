from django.core.paginator import Paginator
from django.shortcuts import render
from home.models import player_key

def home(request):
    objts = player_key.objects.all()
    paginator = Paginator(objts, 6)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'player': objts,
        'page_obj':page_obj
                 
    }
    return render (request, 'home.html', context)
