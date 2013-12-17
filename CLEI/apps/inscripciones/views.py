from django.shortcuts import render

from django.http import HttpResponse

from CLEI.apps.inscripciones.models import Participante
from CLEI.apps.inscripciones.forms import ParticipanteForm
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.
class CreateParticipanteView(CreateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = "inscripciones/create_participante.html"

def get_context_data(self, *args, **kwargs):
        context = super(CreateParticipanteView, self).get_context_data(*args, **kwargs)

        context.update({
            'hola': 'como estas?'
            })

        return context

def get_success_url(self):
        return reverse('ver_participante',args=[self.object.id])

class VerParticipanteView(DetailView):
    model = Participante
    template_name = "inscripciones/ver_participante.html"