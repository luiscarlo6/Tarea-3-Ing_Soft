from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from CLEI.apps.inscripciones.models import Participante, AsistenciaGeneral
from CLEI.apps.inscripciones.forms import ParticipanteForm, RegistrarAsistenciaGeneralForm
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect


def index_view(request):
    return render_to_response('inscripciones/index.html',
                            context_instance = RequestContext(request))

def select_paquete_view(request):
    return render_to_response('inscripciones/select_paquete.html',
                              context_instance = RequestContext(request))

def select_descuento_view(request):
    return render_to_response('inscripciones/select_descuento.html',
                              context_instance = RequestContext(request))
    
def paquete_general_view(request):
    valores_iniciales = {'precio': 250, 'beneficios': 'beneficios', 'eventos':'eventos'}
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarAsistenciaGeneralForm(request.POST, initial = valores_iniciales, readonly_form=True)
            if form.is_valid():
                cp = form.save(commit=False)
                cp.NOMBRE = form.cleaned_data["nombre"]
#                 cp.apellido = form.cleaned_data["apellido"]
#                 cp.institucion = form.cleaned_data["institucion"]
#                 cp.pais = form.cleaned_data["pais"]
                cp.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente"
                
            else:
                info = "Informacion con datos incorrectos"
                
            form = RegistrarAsistenciaGeneralForm(initial = valores_iniciales)
            ctx = {"form":form, "informacion":info}
            return render_to_response('inscripciones/paquete_general.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarAsistenciaGeneralForm(initial = valores_iniciales)
            ctx = {"form":form}
            return render_to_response('inscripciones/paquete_general.html', ctx, 
                                       context_instance = RequestContext(request))
            
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")     

def exclusiva_charlas_view(request):
    return render_to_response('inscripciones/exclusiva_charlas.html',
                              context_instance = RequestContext(request))

def exclusiva_talleres_view(request):
    return render_to_response('inscripciones/exclusiva_talleres.html',
                              context_instance = RequestContext(request))

def exclusiva_talleres_charlas_view(request):
    return render_to_response('inscripciones/exclusiva_talleres_charlas.html',
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
