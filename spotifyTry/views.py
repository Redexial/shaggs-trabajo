from gc import get_objects
from re import L
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest

from spotifyTry.models import Persona
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getPersona(req, usuario):
    print("%s HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEYS"%usuario)
    persona = get_object_or_404(Persona, pk=usuario)
    return HttpResponse("este es el usuario que buscabas %s" %persona)

def updatePersona(req:HttpRequest, usuario):
    persona = get_object_or_404(Persona, pk=usuario)
    #persona.nombres = "Juan"
    #persona.save()
    parsed = json.loads(req.body)
    print(parsed)
    print(parsed["nombres"])
    return HttpResponse("Garcias "+str(req.read()))