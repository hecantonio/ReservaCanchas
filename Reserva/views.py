from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancha, Persona

# Create your views here.

def getInfoCanchaById(request, id_cancha):
    cancha = Cancha.objects.get(id=id_cancha)
    result = f"<h3>Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}</h3>"
    return HttpResponse(result)

def getPersonaById(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    result = f"Nombre: {persona.nombre}<br>Apellido: {persona.apellido}<br>Correo: {persona.correo}"
    return HttpResponse(result)

