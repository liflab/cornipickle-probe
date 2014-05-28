# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('probe_dispatcher.views',
                       url(r'^$', 'probe_list', name="probe_list")
)