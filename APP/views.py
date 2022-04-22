from posixpath import split
from re import template
from django.shortcuts import render
from .models import Diak

def index(request):
    template = "index.html"
    if request.method=="POST":
        sito = request.POST['azonosito']
        template = "megfelelt.html"
        hanincs = "nincs.html"
        alanyok = Diak.objects.filter(azonosito = sito)
        for alany in alanyok:
            if alany.megfelelt == True:
                alany.megfeleltt = "Gratulálunk, felvételt nyert az iskolánkba!"
            else: 
                alany.megfeleltt = "Sajnáljuk nem nyert felvételt!"
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
        i = 0
        for diak in tabla:
            akt = diak.split(",")

            print(akt[0] is not int or akt[1] is not str or akt[2] is not str or akt[3] is not int or akt[4] is not bool and not akt[0] == "")
            print(type(akt[0]))
            try:
                a = int(akt[0])
                b = str(akt[1])
                c = str(akt[2])
                d = int(akt[3])
                e = bool(akt[4])
            except:
                return render(request, template, {'hiba': "Valamelyik adat hibás"})

            if Diak.objects.filter(azonosito=akt[0]).first() == None:
                Diak.objects.create(azonosito=akt[0],nev=akt[1],szak=akt[2],pont=akt[3],megfelelt=akt[4],)
            elif Diak.objects.filter(azonosito=akt[0], szak=akt[2]) == None:
                Diak.objects.create(azonosito=akt[0],nev=akt[1],szak=akt[2],pont=akt[3],megfelelt=akt[4],)
        return render(request, template, {})
    else:
        return render(request, template, {'hiba': "Hibás jelszó"})