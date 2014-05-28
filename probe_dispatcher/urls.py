# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('probe_dispatcher.views',
                       url(r'^$', 'dashboard', name="dashboard"),
                       url(r'^probes$', 'probe_list', name="probes"),
                       url(r'^sensors$', 'probe_list', name="sensors"),
)