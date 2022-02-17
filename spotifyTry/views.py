from gc import get_objects
from re import L
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest

from spotifyTry.models import Ciudad, Persona, TipoDocumento
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def userPersona(req:HttpRequest, usuario):
    print("%s HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEYS"%usuario)
    persona = get_object_or_404(Persona, pk=usuario)
    if req.method == "GET":
        return HttpResponse("este es el usuario que buscabas %s" %persona)
    elif req.method == "DELETE":
        username = persona.usuario
        persona.delete()
        return HttpResponse("usuario %s borrado"%username)
    return 

def updatePersona(req:HttpRequest, usuario):
    persona = get_object_or_404(Persona, pk=usuario)
    #persona.nombres = "Juan"
    #persona.save()
    parsed = json.loads(req.body)
    for trait, value in parsed.items():
        try:
            setattr(persona, trait, value)
        except Exception:
            print(Exception)
    persona.save()
    print(persona)
    return HttpResponse("Garcias "+str(req.read()))

def createPersona(req:HttpRequest, usuario):
    persona = Persona()
    parsed = json.loads(req.body)
    for trait, value in parsed.items():
        try:
            if(trait == "tipodocumento" or trait == "lugarderecidencia"):
                if(trait == "tipodocumento"):
                    print("documento")
                    documento = TipoDocumento()
                    for trait, value in value.items():
                        setattr(documento, trait, value)
                    documento.save()
                    setattr(persona, "tipodocumento", documento)
                else:
                    print("ciudad")
                    ciudad = Ciudad()
                    for trait, value in value.items():
                        setattr(ciudad, trait, value)
                    ciudad.save()
                    setattr(persona, "lugarderecidencia", ciudad)
            setattr(persona, trait, value)
        except BaseException as e:
            print(e)
    persona.save()
    return HttpResponse("persona creada "+ str(persona))

def getDocumento(req:HttpRequest, id):
    documento = get_object_or_404(TipoDocumento, id=id)
    return HttpResponse("Tipo de Documento que busca "+ str(documento))