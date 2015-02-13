from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
                       url(r'^(?P<league_id>\d+)$', views.details, name='details'),
                       url(r'^(?P<league_id>\d+)/edit$', views.edit, name='edit'),
                       url(r'^create$', views.create, name='create')
)
