# -*- coding: utf-8 -*-

from django import forms

from probe_project.apps.probe_dispatcher.models import *


class ProbeForm(forms.ModelForm):
    class Meta:
        model = Probe

    fields = ['name', 'description', 'domain']



