from re import template
from tkinter import Variable
from django.shortcuts import render
from .models import Diak

def index(request):
    template = "index.html"
    if request.method=="POST":
        sito = request.POST['azonosito']
        print(sito)
        
        template = "megfelelt.html"
        hanincs = "nincs.html"
        alany = Diak.objects.filter(azonosito = sito).first()

        if alany != None:
            context={'diak': alany}
            return render(request, template, context)
        else:
            return render(request, hanincs)
        
    return render(request, template)

def feltoltes(request):
    template = "admin.html"
    context = {}
    return render(request, template, context)