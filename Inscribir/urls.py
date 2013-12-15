from django.conf.urls import patterns, url

from Inscribir import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<persona_a_inscribir>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
)