# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('probe_project.apps.probe_dispatcher.views',
                       url(r'^$', 'dashboard', name="dashboard"),
                       url(r'^probes$', 'probes', name="probes"),
                       url(r'^sensors$', 'sensors', name="sensors"),
)