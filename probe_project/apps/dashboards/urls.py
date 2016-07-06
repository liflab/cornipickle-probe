from django.conf.urls import url,include
from django.conf.urls import patterns


urlpatterns = patterns('probe_project.apps.dashboards.views',
                       url(r'^dashboard/?$', 'datum', name="datum"),
                       url(r'^datums/refresh/?$', 'datum_refresh', name="datum_refresh"),
                       url(r'^datums/delete/(?P<datum_id>\d+)/?$', 'datum_delete', name="datum_delete"),
                       url(r'^datums/details/(?P<datum_id>\d+)/?$', 'datum_detail', name="datum_detail"),
                       )