# -*- coding: utf-8 -*-

from django.contrib import admin

from models import *


class ProbeAdmin(admin.ModelAdmin):
    """
    Sponsor admin class
    """

    # ordering = ()
    list_display = ('name', 'domain', 'user', 'sensor_names', 'clickable_probe_url')
    search_fields = ('name', 'description', 'domain', 'id')


class SensorAdmin(admin.ModelAdmin):
    """
    Sensor admin class
    """

    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Probe, ProbeAdmin)
admin.site.register(Sensor, SensorAdmin)
