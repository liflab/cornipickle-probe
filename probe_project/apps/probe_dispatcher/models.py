# -*- coding: utf-8 -*-

import hashlib
import random

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Sensor(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=200
    )

    code = models.TextField(
        verbose_name=("Code"),
        default=("")
    )

    def __unicode__(self):
        return self.name


class Probe(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Name of the probe"),
        editable=True,
        max_length=255
    )

    description = models.TextField(
        verbose_name=_("Description"),
        max_length=1200,
    )

    domain = models.CharField(
        verbose_name=_("Domain"),
        max_length=200
    )

    hash = models.CharField(
        verbose_name=_("Hash"),
        max_length=40,
        editable=False,
    )

    # todo: make this a list or a foreign key, something like that
    sensors = models.ManyToManyField(
        Sensor
    )

    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        unique=False,
        help_text=_("Owner of the probe")
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

    def probe_url(self, id=settings.SITE_ID):
        current_site = Site.objects.get(id=id)
        return "http://" + current_site.domain + '/p/' + self.id.__str__() + '_' + self.hash.__str__() + '.js'

    # makes the url clickable in the admin table
    def clickable_probe_url(self):
        probe_url = self.probe_url()
        return '<a href="%s" target="_blank">%s</a>' % (probe_url, probe_url)

    def get_script_tag(self):
        probe_url = self.probe_url()
        return '<script type="application/javascript" src="%s"></script>' % (probe_url)

    def sensor_names(self):
        return ', '.join([sensor.name for sensor in self.sensors.all()])

    sensor_names.short_description = "Sensors"

    clickable_probe_url.allow_tags = True
    clickable_probe_url.short_description = 'url'
