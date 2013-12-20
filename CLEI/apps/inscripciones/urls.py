from django.conf.urls import patterns, url 
from CLEI.apps.inscripciones.views import CreateParticipanteView,\
    VerInscripcionView, CreateGeneralView


urlpatterns = patterns('CLEI.apps.inscripciones.views',
                       url(r'^$', 'index_view', name='vista_principal'),
                       
                       url(r'^create/$', CreateParticipanteView.as_view(), name='crear_participante'),

                       url(r'^paquete/$', 'select_paquete_view', name='vista_seleccion_paquete'),

                       url(r'^general/$', CreateGeneralView.as_view(), name='vista_paquete_general'),  
                       
#                        url(r'^create/(?P<pk>[\w]+)/paquete/general/descuento/$', 'select_descuento_view', name='vista_seleccion_descuento'),
# 
#                        url(r'^paquete/exclusiva_charla$', 'exclusiva_charlas_view', name='vista_exclusiva_charlas'),
# 
#                        url(r'^paquete/exclusiva_talleres$', 'exclusiva_talleres_view', name='vista_exclusiva_talleres'),
# 
#                        url(r'^paquete/exclusiva_talleres_charlas$', 'exclusiva_talleres_charlas_view', name='vista_exclusiva_talleres_charlas'),                       

                       url(r'^ver/(?P<pk>[\w]+)/$', VerInscripcionView.as_view(), 
                           name='ver_inscripcion'),
                       )
