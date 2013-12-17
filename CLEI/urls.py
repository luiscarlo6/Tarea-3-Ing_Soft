from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^inscripcion/', include('CLEI.apps.inscripciones.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
