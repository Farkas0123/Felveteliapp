from posixpath import split
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
    template = "upload.html"
    if request.method =="POST" and request.POST['jelszo']=="jelszo":
        tabla = request.POST['adatok'].split("\t")
        for diak in tabla:
            akt = diak.split(",")
            if Diak.objects.filter(azonosito=akt[0]).first() == None:
                Diak.objects.create(azonosito=akt[0],nev=akt[1],szak=akt[2],pont=akt[3],megfelelt=akt[4],)
                alert('Feltöltve')
                

            


    context = {}
    return render(request, template, context)