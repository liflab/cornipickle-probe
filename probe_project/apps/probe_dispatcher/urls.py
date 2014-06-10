# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('probe_project.apps.probe_dispatcher.views',
                       url(r'^$', 'dashboard', name="dashboard"),
                       url(r'^probe/(?P<id>\d+)/', 'probe_detail', name='probe_form'),
                       url(r'^probes$', 'probes', name="probes"),
                       url(r'^probes/create/', 'probe_form', name='probe_form'),
                       url(r'^sensors$', 'sensors', name="sensors"),
)