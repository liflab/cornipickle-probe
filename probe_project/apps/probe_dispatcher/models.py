# -*- coding: utf-8 -*-

import hashlib
import random

from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
import requests
import urllib
import jsonfield
import json


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

    is_valid = models.BooleanField(
        verbose_name=_("Code validity"),
        default=False,
        help_text=_("Code validity"),
        editable=False
    )

    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        unique=False,
        help_text=_("Owner of the sensor"),
    )

    def __unicode__(self):
        return str("{0} - {1}".format(self.id,self.name))

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

    def check_syntax(self):
        data = json.dumps({"action":"parse","code":self.code})
        r = requests.post(url="http://localhost:11019/fiddle/", data=urllib.quote_plus(data))
        r = r.json()
        return r["isValid"]

    def save(self,*args,**kwargs):
        self.is_valid = self.check_syntax() == "true"
        super(Sensor, self).save(*args, **kwargs)


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
        verbose_name= _("Sensor"),
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

    tags_attributes_interpreter = jsonfield.JSONField(
        default={'tagnames': '', 'attributes': '', 'interpreter': ''},
        null=False,
        editable=False,
    )

    # domains = models.

    def save(self,*args,**kwargs):
        if not self.pk:
            # This code only happens if the objects is
            # not in the database yet. Otherwise it would
            # have pk
            s = str(random.random())
            user = self.user.__str__()
            name = self.name.encode('utf-8')
            self.hash = hashlib.sha1(s + user + name).hexdigest()
        super(Probe, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def add_property(self):
        url = 'http://localhost:11019/add'
        text = ''
        for sensor in self.sensors.all():
            text = text + sensor.code + "\n\n"
        text = urllib.quote_plus(text)
        r = requests.post(url, data=text)
        if r.status_code == 200:
            self.tags_attributes_interpreter = r.json()
        else:
            self.tags_attributes_interpreter = {'tagnames': '', 'attributes': '', 'interpreter': ''}
            self.is_enabled = False

    def checkValidity(self):
        valid = True
        for sensor in self.sensors.all():
            if not sensor.is_valid:
                valid = False
                break
        return valid

    # makes the url clickable in the admin table
    def clickable_probe_url(self):
        script_url = self.get_script_url()
        return '<a href="%s" target="_blank">%s</a>' % (script_url, script_url)

    def get_script_tag(self):
        script_url = self.get_script_url()
        return '<script type="application/javascript" src="%s"></script>' % (script_url)

    def get_script_url(self):
            current_site = Site.objects.get_current().domain
            return 'http://' + current_site + '/p/' + self.id.__str__() + '_' + self.hash.__str__() + '.js'

    def sensor_names(self):
        return ', '.join([sensor.name for sensor in self.sensors.all()])

    sensor_names.short_description = "Sensors"

    clickable_probe_url.allow_tags = True
    clickable_probe_url.short_description = 'url'
