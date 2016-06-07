# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model

from probe_project.apps.probe_dispatcher.models import *


class ProbeFrontendForm(forms.ModelForm):

    class Meta:
        model = Probe
        exclude = ('user',)

class SensorFrontendForm(forms.ModelForm):
    class Meta:
        model = Sensor
        exclude = ('user',)
