from django.conf.urls import patterns, url
from CLEI.apps.inscripciones.views import CreateParticipanteView,\
    VerParticipanteView


urlpatterns = patterns('CLEI.apps.inscripciones.views',
                       url(r'^$', 'index_view', name='vista_principal'),
                       url(r'^paquete/$', 'select_paquete_view', name='vista_seleccion_paquete'),
                       url(r'^descuento/$', 'select_descuento_view', name='vista_seleccion_descuento'),
                       url(r'^create/$', CreateParticipanteView.as_view(), 
        name='crear_participante'),
                        url(r'^ver/(?P<pk>[\w]+)/$', VerParticipanteView.as_view(), 
        name='ver_participante'),
                       )
