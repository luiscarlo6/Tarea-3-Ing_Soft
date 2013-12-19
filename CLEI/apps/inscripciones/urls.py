from django.conf.urls import patterns, url
from CLEI.apps.inscripciones.views import CreateParticipanteView,\
    VerParticipanteView, CreatePaqueteView


urlpatterns = patterns('CLEI.apps.inscripciones.views',
                       url(r'^$', 'index_view', name='vista_principal'),
                       
                       url(r'^create/$', CreateParticipanteView.as_view(), name='crear_participante'),

                       url(r'^create/(?P<pk>[\w]+)/paquete/$', CreatePaqueteView.as_view(), name='vista_seleccion_paquete'),

                       url(r'^create/(?P<pk>[\w]+)/paquete/general$', 'paquete_general_view', name='vista_paquete_general'),

                       url(r'^paquete/exclusiva_charla$', 'exclusiva_charlas_view', name='vista_exclusiva_charlas'),

                       url(r'^paquete/exclusiva_talleres$', 'exclusiva_talleres_view', name='vista_exclusiva_talleres'),

                       url(r'^paquete/exclusiva_talleres_charlas$', 'exclusiva_talleres_charlas_view', name='vista_exclusiva_talleres_charlas'),

                       url(r'^descuento/$', 'select_descuento_view', name='vista_seleccion_descuento'),

                       

                       url(r'^ver/(?P<pk>[\w]+)/$', VerParticipanteView.as_view(), 
                           name='ver_participante'),
                       )
