from CLEI.apps.inscripciones.views import CreateParticipanteView, \
    VerParticipanteView, SelectPaqueteView
from django.conf.urls import patterns, url


urlpatterns = patterns('CLEI.apps.inscripciones.views',
   url(r'^$', 'index_view' , name='vista_principal'),
   
   url(r'^create/$', CreateParticipanteView.as_view(),
        name='crear_participante'),
                       
   url(r'^ver/(?P<pk>[\w]+)/$', VerParticipanteView.as_view(),
        name='ver_participante'),
                       
   url(r'^select/$', SelectPaqueteView.as_view(),
        name='seleccionar_paquete'),
    
)
