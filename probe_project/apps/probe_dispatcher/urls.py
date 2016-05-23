# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('probe_project.apps.probe_dispatcher.views',
                       url(r'^$', 'dashboard', name="dashboard"),
                       url(r'^probe/(?P<probe_id>\d+)/?$', 'probe_detail', name='probe_detail'),
                       url(r'^probes/?$', 'probes', name="probes"),
                           url(r'^probes/create/?$', 'probe_form', name='probe_form'),
                       url(r'^probes/edit/(?P<probe_id>\d+)/?$', 'probe_form', name='probe_edit'),
                       url(r'^probes/delete/(?P<probe_id>\d+)/?$', 'probe_delete', name='probe_delete'),
                       url(r'^probes/add_corni/(?P<probe_id>\d+)/?$', 'probe_add_corni', name='probe_add_corni'),
                       url(r'^sensors/?$', 'sensors', name="sensors"),
                       url(r'^sensors/create/?$', 'sensor_form', name='sensor_form'),
                       url(r'^sensors/edit/(?P<sensor_id>\d+)/?$', 'sensor_form', name='sensor_edit'),
                       url(r'^sensors/(?P<sensor_id>\d+)/?$', 'sensor_detail', name='sensor_detail'),
                       url(r'^sensors/delete/(?P<sensor_id>\d+)/?$', 'sensor_delete', name='sensor_delete'),
)