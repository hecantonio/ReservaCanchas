from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancha, Persona, Horario
from django.views.generic import TemplateView



# Create your views here.

def getInfoCanchaById(request, id_cancha):
    cancha = Cancha.objects.get(id=id_cancha)
    horarios = Horario.objects.filter(cancha_id= cancha.id)
    #result = f"<h3>Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}</h3>"
    #return HttpResponse(result)
    return render(request, 'cancha.html', { 'nombre_cancha': cancha.nombre, 'desc_cancha': cancha.descripcion, 'horarios' : horarios})


def getInfoPersonaById(request ,id_persona):
    #obtener Persona por su id
    persona = Persona.objects.get(id=id_persona)
    result = f"Cancha: {persona.nombre}, Descripción: {persona.apellido} y tu correo es {persona.correo} ."
    return HttpResponse(result)

class MainView(TemplateView):
    template_name = "main.html"

def getListadoCanchas(request ):
    canchas = Cancha.objects.all()
    nombre_canchas = []
    for cancha in canchas:
        nombre_canchas.append((cancha.id, cancha.nombre))

    return render(request, "canchas.html", {'listado':nombre_canchas})
