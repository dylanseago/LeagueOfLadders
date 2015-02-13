from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^l/', include('leagueofladders.apps.myleague.urls', namespace='myleague')),
                       url(r'^admin/', include(admin.site.urls)),
)
