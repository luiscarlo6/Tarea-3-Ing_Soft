from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from CLEI.apps.clei.forms import RegistrarMiembroCP, RegistrarArticuloForm
from CLEI.apps.clei.forms import RegistrarEvaluacionForm

from CLEI.apps.clei.models import Articulo, MiembroCP, Evaluacion

def index_view(request):
    return render_to_response('index.html',
                               context_instance = RequestContext(request))
    

def registrar_miembroCP_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarMiembroCP(request.POST)
            if form.is_valid():
                cp = form.save(commit=False)
                cp.nombre = form.cleaned_data["nombre"]
                cp.apellido = form.cleaned_data["apellido"]
                cp.institucion = form.cleaned_data["institucion"]
                cp.pais = form.cleaned_data["pais"]
                cp.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente"
                
            else:
                info = "Informacion con datos incorrectos"
                
            form = RegistrarMiembroCP()
            ctx = {"form":form, "informacion":info}
            return render_to_response('registrarMiembroCP.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarMiembroCP()
            ctx = {"form":form}
            return render_to_response('registrarMiembroCP.html', ctx, 
                                       context_instance = RequestContext(request))
            
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")     
    

def registrar_articulo_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrarArticuloForm(request.POST)
            if form.is_valid():
                articulo = form.save(commit=False)
                articulo.titulo = form.cleaned_data["titulo"]
                articulo.p1 = form.cleaned_data["p1"]
                articulo.p2 = form.cleaned_data["p2"]
                articulo.p3 = form.cleaned_data["p3"]
                articulo.p4 = form.cleaned_data["p4"]
                articulo.p5 = form.cleaned_data["p5"]
                #articulo.status = form.cleaned_data["status"]
                articulo.save()
                form.save_m2m()
                info = "Se guardo satisfactoriamente"
                
            else:
                info = "Informacion con datos incorrectos"
                
            form = RegistrarArticuloForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('registrarArticulo.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            form = RegistrarArticuloForm()
            ctx = {"form":form}
            return render_to_response('registrarArticulo.html', ctx, 
                                       context_instance = RequestContext(request))
            
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/") 
    
    
def registrar_evaluacion_view(request):
    if request.user.is_authenticated(): 
        if request.method == 'POST': # Si la request es PO
            form = RegistrarEvaluacionForm(request.POST)
            if form.is_valid():
                nueva_eval = Evaluacion()
                nueva_eval.articulo = form.cleaned_data["articulo"]
                nueva_eval.miembro_cp = form.cleaned_data["miembro_cp"]
                nueva_eval.nota = form.cleaned_data["nota"]
                #Verificamos que coincidan los topicos del cp y del articulo
                if not nueva_eval.coinciden_topicos():
                    info = "ERROR. Los topicos no coinciden"
                    form = RegistrarEvaluacionForm()
                    ctx = {"form":form, "informacion":info}
                    return render_to_response('registrarEvaluacion.html', ctx, 
                                              context_instance = RequestContext(request))
                else:
                    if nueva_eval.existe_evaluacion():
                        info = "ERROR. Evaluacion ya existe"
                        form = RegistrarEvaluacionForm()
                        ctx = {"form":form, "informacion":info}
                        return render_to_response('registrarEvaluacion.html', ctx, 
                                              context_instance = RequestContext(request))
                    
                nueva_eval.save()
                info = "Se guardo satisfactoriamente"
                
            else:
                info = "Informacion con datos incorrectos"
                
            form = RegistrarEvaluacionForm()
            ctx = {"form":form, "informacion":info}
            return render_to_response('registrarEvaluacion.html', ctx, 
                                       context_instance = RequestContext(request))
        # Si el request es un GET    
        else:
            info = ""
            form = RegistrarEvaluacionForm()
            ctx = {"form":form}
            return render_to_response('registrarEvaluacion.html', ctx, 
                                       context_instance = RequestContext(request))
            
    #Si el usuario no esta autenticado
    else:
        return HttpResponseRedirect("/")     
            
        