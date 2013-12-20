from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from CLEI.apps.inscripciones.models import Participante, Inscripcion
from CLEI.apps.inscripciones.forms import ParticipanteForm, InscripcionForm
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

def exclusiva_charlas_view(request):
    return render_to_response('inscripciones/exclusiva_charlas.html',
                              context_instance = RequestContext(request))

def exclusiva_talleres_view(request):
    return render_to_response('inscripciones/exclusiva_talleres.html',
                              context_instance = RequestContext(request))

def exclusiva_talleres_charlas_view(request):
    return render_to_response('inscripciones/exclusiva_talleres_charlas.html',
                              context_instance = RequestContext(request))
                              
class CreateGeneralView(CreateView):
    persona = None
    model = Inscripcion
    form_class = InscripcionForm
    template_name = "inscripciones/paquete_general.html"
    #    initial = {'precio': 250, 'beneficios': 'beneficios', 'eventos':'eventos'}
    initial = {'persona' :Participante.objects.last()}
    def get_context_data(self, *args, **kwargs):
        context = super(CreateGeneralView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_inscripcion',args=[self.object.id])

class CreateParticipanteView(CreateView):
    model = Participante
    form_class = ParticipanteForm 
    template_name = "inscripciones/create_participante.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(CreateParticipanteView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('vista_seleccion_paquete')

class VerInscripcionView(DetailView):
    model = Inscripcion
    template_name = "inscripciones/ver_inscripcion.html"
