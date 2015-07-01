# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('probe_project.apps.probe_dispatcher.views',
                       url(r'^$', 'dashboard', name="dashboard"),
                       url(r'^probe/(?P<probe_id>\d+)/?$', 'probe_detail', name='probe_detail'),
                       url(r'^probes/?$', 'probes', name="probes"),
                       url(r'^probes/create/?$', 'probe_form', name='probe_form'),
                       url(r'^probes/edit/(?P<probe_id>\d+)/?$', 'probe_form', name='probe_edit'),
                       url(r'^probes/delete/(?P<probe_id>\d+)/?$', 'probe_delete', name='probe_delete'),
                       url(r'^sensors/?$', 'sensors', name="sensors"),
)