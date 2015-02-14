from django.conf.urls import patterns, include, url
from django.contrib import admin

from leagueofladders import settings


urlpatterns = patterns('',
                       url(r'^l/', include('leagueofladders.apps.myleague.urls', namespace='myleague')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^%s$' % settings.LOGIN_URL[1:], 'django.contrib.auth.views.login'))
