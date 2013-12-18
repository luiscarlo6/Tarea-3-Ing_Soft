from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from CLEI.apps.inscripciones.models import Participante
from CLEI.apps.inscripciones.forms import ParticipanteForm
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView


def index_view(request):
    return render_to_response('inscripciones/index.html',
                              context_instance = RequestContext(request))

def select_paquete_view(request):
    return render_to_response('inscripciones/select_paquete.html',
                              context_instance = RequestContext(request))

def select_descuento_view(request):
    return render_to_response('inscripciones/select_descuento.html',
                              context_instance = RequestContext(request))
class CreateParticipanteView(CreateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = "inscripciones/create_participante.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CreateParticipanteView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_participante',args=[self.object.id])

class VerParticipanteView(DetailView):
    model = Participante
    template_name = "inscripciones/ver_participante.html"