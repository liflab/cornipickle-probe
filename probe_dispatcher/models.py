# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import get_current_site
from django.http import request


class Sensor(models.Model):
    name = models.CharField(
        max_length=200
    )

    def __unicode__(self):
        return self.name


class Probe(models.Model):
    name = models.CharField(
        verbose_name=u"name",
        help_text=u"Name of the probe",
        editable=True,
        max_length=255
    )

    description = models.TextField(
        max_length=1200,
    )

    domain = models.CharField(
        max_length=200
    )

    # todo: make this a list or a foreign key, something like that
    sensors = models.ManyToManyField(
        Sensor
    )

    user = models.ForeignKey(
        User,
        unique=False,
        verbose_name=u"user",
        help_text=u"User"
    )

    def __unicode__(self):
        return self.name

    class Meta:
        pass

    def probe_url(self):
        return get_current_site(request) + 'probe/' + self.id

    # makes the url clickable in the admin table
    def clickable_probe_url(self):
        return '<a href="%s" target="_blank">%s</a>' % (self.probe_url(), self.probe_url())

    def sensor_names(self):
        return ', '.join([sensor.name for sensor in self.sensors.all()])

    sensor_names.short_description = "Sensors"

    clickable_probe_url.allow_tags = True
    clickable_probe_url.short_description = 'Website'
