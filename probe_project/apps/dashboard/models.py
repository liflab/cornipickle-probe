import ast
import calendar
import datetime

import feedparser
import requests

from django.db import models, connections
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation,
)
from django_hosts.resolvers import reverse
from django.utils.translation import ugettext_lazy as _
from probe_project.apps.probe_dispatcher.models import Probe
from probe_project.apps.accounts.models import User
from django.contrib.contenttypes.models import ContentType


"""
Datum is a single Data
"""

class Datum(models.Model):
    probeId = models.ForeignKey(Probe)
    httpReferer = models.CharField(max_length=255)
    httpUserAgent = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    OS = models.CharField(max_length=255)
    slug = models.SlugField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        unique=False,
        help_text=_("Owner of the probe")
    )



