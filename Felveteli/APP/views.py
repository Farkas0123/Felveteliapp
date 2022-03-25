from re import template
from django.shortcuts import render
from .models import Diak

def megfelelt(request):
    print(request.POST)
    if request.method=="POST":
        sito = request.POST['azonosito']
    
    megfelelt = "megfelelt.html"
    hanincs = "nincs.html"

    alany = Diak.objects.filter(azonosito = sito).first()

    if alany != None:
        context={'diak': alany}
        return render(request, megfelelt, context)
    else:
        return render(request, hanincs)
    
def index(request):
    template = "index.html"
    return render(request, template)
    