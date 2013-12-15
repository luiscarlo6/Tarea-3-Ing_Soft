from django.shortcuts import render
from django.http import HttpResponse
from Inscribir.models import Inscripcion

def index(request):
    latest_poll_list = Inscripcion.objects.order_by('persona_a_inscribir')[:5]
    output = ', '.join([p.persona_a_inscribir for p in latest_poll_list])
    return HttpResponse(output)

def detail(request, persona_a_inscribir):
    return HttpResponse("persona nuemero %s en inscribirse." % persona_a_inscribir)

def results(request, poll_id):
    return HttpResponse("persona aaaanuemero %s en inscribirse." % poll_id)