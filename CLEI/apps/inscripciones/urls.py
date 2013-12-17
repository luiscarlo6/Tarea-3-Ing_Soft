from django.conf.urls import patterns, url

from CLEI.apps.inscripciones.views import CreateParticipanteView, VerParticipanteView 

urlpatterns = patterns('',
     url(r'^create/$', CreateParticipanteView.as_view(), 
        name='crear_participante'),
    url(r'^ver/(?P<pk>[\w]+)/$', VerParticipanteView.as_view(), 
        name='ver_participante'),
    
)