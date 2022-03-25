from django.shortcuts import render
from .models import Diak

def index(request):
    if request.method=="POST":
        sito = request.POST['azonosito']
    
    template = "index.html"
    hanincs = "nincs.html"

    alany = Diak.objects.filter(azonosito = sito).first()

    if alany != None:
        context={'Feri': alany}
        return render(request, template, context)
    else:
        return render(request, hanincs)
    
    