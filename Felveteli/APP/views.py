from posixpath import split
from re import template
from tkinter import Variable
from django.shortcuts import render
from .models import Diak

def index(request):
    template = "index.html"
    if request.method=="POST":
        sito = request.POST['azonosito']
        template = "megfelelt.html"
        hanincs = "nincs.html"
        alanyok = Diak.objects.filter(azonosito = sito)
        if alanyok.first() != None:
            context={'diakok': alanyok}
            return render(request, template, context)
        else:
            return render(request, hanincs, {})
        
    return render(request, template, {})

def feltoltes(request):
    template = "upload.html"
    if request.method =="POST" and request.POST['jelszo']=="jelszo":
        tabla = request.POST['adatok'].split("\t")
        for diak in tabla:
            akt = diak.split(",")
            print(Diak.objects.filter(azonosito=akt[0]).first().azonosito == akt[0])
            print(Diak.objects.filter(azonosito=akt[0]).first().szak != akt[2])
            d = Diak.objects.filter(azonosito=akt[0]).first()
            if d == None:
                Diak.objects.create(azonosito=akt[0],nev=akt[1],szak=akt[2],pont=akt[3],megfelelt=akt[4],)
            elif Diak.objects.filter(azonosito=akt[0]).first().szak != akt[2]:
                print(f'bent vok {d}')
                Diak.objects.create(azonosito=akt[0],nev=akt[1],szak=akt[2],pont=akt[3],megfelelt=akt[4],)
    context = {}
    return render(request, template, context)