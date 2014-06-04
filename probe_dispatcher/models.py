# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from picklefield.fields import PickledObjectField

from probe_app.settings import DEBUG

import hashlib
import random

class SensorType(models.Model):
    template_name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        max_length=1200,
    )

    prototype_properties = PickledObjectField()

    prototype_data = PickledObjectField()

class Browser(models.Model):
    date = models.DateTimeField(
        auto_now=True,
    )

    user_agent = models.CharField(
        max_length = 200,
    )

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

    hash = models.CharField(
        max_length=40,
        editable = False,
    )

    user = models.ForeignKey(
        User,
        unique=False,
        verbose_name=u"user",
        help_text=u"User"
    )

    # domains = models.

    def __unicode__(self):
        return self.name

    class Meta:
        pass

    def save(self, *args, **kwargs):
        if not self.pk:
            #This code only happens if the objects is
            #not in the database yet. Otherwise it would
            #have pk
            s = str(random.random())
            user = self.user.__str__()
            name = self.name.encode('utf-8')
            self.hash = hashlib.sha1(s + user + name).hexdigest()
        super(Probe, self).save(*args, **kwargs)

    def probe_url(self, name='Prod'):
        current_site = Site.objects.get(name=name)
        return "http://" + current_site.domain + '/p/' + self.id.__str__() + '_' + self.hash.__str__() + '.js'

    # makes the url clickable in the admin table
    def clickable_probe_url(self):
        if DEBUG:
            probe_url = self.probe_url('dev')
        else:
            probe_url = self.probe_url()
        return '<a href="%s" target="_blank">%s</a>' % (probe_url, probe_url)

    def get_script_tag(self):
        if DEBUG:
            probe_url = self.probe_url('dev')
        else:
            probe_url = self.probe_url()
        return '<script type="application/javascript" src="%s"></script>' % (probe_url)

    def sensor_names(self):
        return ', '.join([sensor.name for sensor in self.sensors.all()])

    sensor_names.short_description = "Sensors"

    clickable_probe_url.allow_tags = True
    clickable_probe_url.short_description = 'url'

class Sensor(models.Model):
    name = models.CharField(
        max_length=200
    )

    probe = models.ForeignKey(Probe)
    
    sensor_type = models.ForeignKey(SensorType)

    properties = PickledObjectField()

    description = models.TextField(
        max_length=1200,
    )

    def __unicode__(self):
        return self.name

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor)
    
    browser = models.ForeignKey(Browser)

    data = PickledObjectField()

    datetime = models.DateTimeField(
        auto_now=True,
    )
