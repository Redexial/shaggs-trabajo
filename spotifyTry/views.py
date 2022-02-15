from gc import get_objects
from re import L
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from spotifyTry.models import Persona

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getPersona(req, usuario):
    print("%s HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEYS"%usuario)
    persona = get_object_or_404(Persona, pk=usuario)
    return HttpResponse("este es el usuario que buscabas %s" %persona)