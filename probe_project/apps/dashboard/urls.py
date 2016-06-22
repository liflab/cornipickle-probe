from django.conf.urls import url,include
from django.conf.urls import patterns


urlpatterns = patterns('probe_project.apps.dashboard.views',
                       url(r'^dashboard?$', 'datum', name="datum"),
                       )