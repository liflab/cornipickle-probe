# -*- coding: utf-8 -*-

import hashlib
import random

from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import subprocess
import requests
import urllib
import jsonfield
import time


class Sensor(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=200,
        help_text=_("Name of the sensor")
    )

    code = models.TextField(
        verbose_name=_("Code"),
        default="",
        help_text=_("Code in the Cornipickle language"),
    )

    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        unique=False,
        help_text=_("Owner of the sensor"),
    )

    def __unicode__(self):
        return self.name


    def check_delete_if_Sensor_is_presente_in_Probe(self,sensor_id):
        """
        Regarde si un Sensor est présent dans un Probe.
        :param sensor_id: L'id du sensor a regarder
        :return: Delete si le sensor n'est present dans aucun probe si non, message d'erreur
        """

        list_probe = Probe.objects.all().filter(sensors=sensor_id)

        if len(list_probe) != 0:
            output = _("You cannot delete the Sensor id {0}, because is use by probe id {1}".format(sensor_id,list_probe[0].id))
            raise ValueError(output)

        self.delete()


class Probe(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Name of the probe"),
        editable=True,
        max_length=255,
    )

    description = models.TextField(
        verbose_name=_("Description"),
        max_length=1200,
        help_text=_("Description of the probe"),
    )

    domain = models.CharField(
        verbose_name=_("Domain"),
        max_length=200,
        help_text=_("Domain the probe will be attached to"),
    )

    hash = models.CharField(
        verbose_name=_("Hash"),
        max_length=40,
        editable=False,
    )

    is_enabled = models.BooleanField(
        verbose_name=_("Enabled"),
        default=False,
        help_text=_("Check the box if you want the probe to be enabled"),
    )

    # todo: make this a list or a foreign key, something like that
    sensors = models.ManyToManyField(
        Sensor,
        blank=True,
        help_text=_("Sensors to be used by the probe (Use CTRL + Left Mouse Button to select)"),
    )

    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        unique=False,
        help_text=_("Owner of the probe")
    )

    pid = models.IntegerField(
        verbose_name="pid",
        blank=True,
        editable=False,
        null=True
    )

    tags_and_attributes = jsonfield.JSONField(
        default={},
        null=False,
        editable=False,
    )

    # domains = models.

    def __unicode__(self):
        return self.name

    class Meta:
        pass

    def save(self, *args, **kwargs):
        if not self.pk:
            # This code only happens if the objects is
            # not in the database yet. Otherwise it would
            # have pk
            s = str(random.random())
            user = self.user.__str__()
            name = self.name.encode('utf-8')
            self.hash = hashlib.sha1(s + user + name).hexdigest()
        super(Probe, self).save(*args, **kwargs)
        if self.is_enabled and not self.pid:
            self.run_parser()
        elif not self.is_enabled and self.pid:
            self.kill_parser()

    def probe_url(self, id=settings.SITE_ID):
        current_site = Site.objects.get(id=id)
        return "http://localhost:8000" + '/p/' + self.id.__str__() + '_' + self.hash.__str__() + '.js'

    # makes the url clickable in the admin table
    def clickable_probe_url(self):
        probe_url = self.probe_url()
        return '<a href="%s" target="_blank">%s</a>' % (probe_url, probe_url)

    def get_script_tag(self):
        probe_url = self.probe_url()
        return '<script type="application/javascript" src="%s"></script>' % (probe_url)

    def sensor_names(self):
        return ', '.join([sensor.name for sensor in self.sensors.all()])

    def run_parser(self):
        p = subprocess.Popen(["java", "-jar", "cornipickle/cornipickle.jar", "-p", str(11000 + self.id)])
        self.pid = p.pid
        f = open('pids.txt', 'a')
        f.write(str(p.pid) + '\n')
        f.close()
        self.save()

    def kill_parser(self):
        print("Killing parser....")
        subprocess.call(["kill", str(self.pid), ])
        self.pid = None
        self.save()

    def add_property(self):
        port = str(11000 + self.id)
        url = 'http://localhost:' + port + '/add'
        text = ''
        for sensor in self.sensors.all():
            text = text + sensor.code + "\n\n"
        text = urllib.quote_plus(text)
        r = requests.put(url, data=text)
        self.tags_and_attributes = r.json()
        self.save()

    sensor_names.short_description = "Sensors"

    clickable_probe_url.allow_tags = True
    clickable_probe_url.short_description = 'url'
