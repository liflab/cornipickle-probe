# -*- coding: utf-8 -*-

from django import forms

from models import *


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Probe



