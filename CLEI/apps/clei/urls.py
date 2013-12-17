from django.conf.urls import patterns, url

urlpatterns = patterns = patterns('CLEI.apps.clei.views',
        url(r'^$', 'index_view', name='vista_principal'),
        url(r'^registrar/miembrocp/$', 'registrar_miembroCP_view', name="vista_registrar_miembrocp"),
        url(r'^registrar/articulo/$', 'registrar_articulo_view', name="vista_registrar_articulo"),
        url(r'^registrar/evaluacion/$', 'registrar_evaluacion_view', name="vista_registrar_evaluacion"),
        )


