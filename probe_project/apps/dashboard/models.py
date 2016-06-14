import ast
import calendar
import xmlrpc.client
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
from django.contrib.contenttypes.models import ContentType



METRIC_PERIOD_INSTANT = _('instant')
METRIC_PERIOD_DAILY = _('daily')
METRIC_PERIOD_WEEKLY = _('weekly')
METRIC_PERIOD_CHOICES = (
    (METRIC_PERIOD_INSTANT, _('Instant')),
    (METRIC_PERIOD_DAILY, _('Daily')),
    (METRIC_PERIOD_WEEKLY, _('Weekly')),
)

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=300,
        help_text=_("Name of the Category in the Dashboard")
    )
    position = models.PositiveSmallIntegerField(
        verbose_name=_("Position"),
        default=1
        )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Metric(models.Model):
    name = models.CharField(max_length=300)
    """
    http://stackoverflow.com/questions/427102/what-is-a-slug-in-django

    Un SlugField permet de mettre un standart sur l'url
    """
    slug = models.SlugField()

    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.SET_NULL)
    position = models.PositiveSmallIntegerField(default=1)
    data = GenericRelation('Datum')
    show_on_dashboard = models.BooleanField(default=True)
    show_sparkline = models.BooleanField(default=True)
    period = models.CharField(max_length=15, choices=METRIC_PERIOD_CHOICES,
                              default=METRIC_PERIOD_INSTANT)
    unit = models.CharField(max_length=100)
    unit_plural = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("metric-detail", args=[self.slug], host='dashboard')

    @property
    def display_position(self):
        cat_position = -1 if self.category is None else self.category.position
        return cat_position, self.position

    def gather_data(self, since):
        """
        Gather all the data from this metric since a given date.
        Returns a list of (timestamp, value) tuples. The timestamp is a Unix
        timestamp, coverted from localtime to UTC.
        """
        if self.period == METRIC_PERIOD_INSTANT:
            return self._gather_data_instant(since)
        elif self.period == METRIC_PERIOD_DAILY:
            return self._gather_data_periodic(since, 'day')
        elif self.period == METRIC_PERIOD_WEEKLY:
            return self._gather_data_periodic(since, 'week')
        else:
            raise ValueError("Unknown period: %s", self.period)

    def _gather_data_instant(self, since):
        """
        Gather data from an "instant" metric.
        Instant metrics change every time we measure them, so they're easy:
        just return every single measurement.
        """
        data = (self.data.filter(timestamp__gt=since)
                         .order_by('timestamp')
                         .values_list('timestamp', 'measurement'))
        return [(calendar.timegm(t.timetuple()), m) for (t, m) in data]

    def _gather_data_periodic(self, since, period):
        """
        Gather data from "periodic" merics.
        Period metrics are reset every day/week/month and count up as the period
        goes on. Think "commits today" or "new tickets this week".
        XXX I'm not completely sure how to deal with this since time zones wreak
        havoc, so there's right now a hard-coded offset which doesn't really
        scale but works for now.
        """
        OFFSET = "2 hours"  # HACK!
        ctid = ContentType.objects.get_for_model(self).id

        c = connections['default'].cursor()
        c.execute('''SELECT
                        DATE_TRUNC(%s, timestamp - INTERVAL %s),
                        MAX(measurement)
                     FROM dashboard_datum
                     WHERE content_type_id = %s
                       AND object_id = %s
                       AND timestamp >= %s
                     GROUP BY 1;''', [period, OFFSET, ctid, self.id, since])
        return [(calendar.timegm(t.timetuple()), float(m)) for (t, m) in c.fetchall()]




class Datum(models.Model):
    metric = GenericForeignKey()
    content_type = models.ForeignKey(ContentType, related_name='+', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    measurement = models.BigIntegerField()

    class Meta:
        ordering = ['-timestamp']
        get_latest_by = 'timestamp'
        verbose_name_plural = 'data'

    def __str__(self):
        return "%s at %s: %s" % (self.metric, self.timestamp, self.measurement)

class EventType(models.Model):
    type = models.CharField(
        verbose_name=_("Type"),
        max_length=200,
        help_text=_("What's the type of the event trigger")
    )

    severity = models.CharField(
        verbose_name=_("Severity"),
        max_length=255,
        help_text=("The importance Event")
    )

class Event(models.Model):
    event_type =  models.ForeignKey(
        EventType,
        verbose_name=_("Event Type"),
        help_text=_("What's is the event type")
    )
    trigger_time = models.TimeField(
        verbose_name= _("Trigger Time"),
        auto_now_add=True
    )

    navigateur = models.CharField(
        verbose_name=_("Web Browser"),
        max_length=255,
        help_text= _("Which web Browser was used went the error was produced")
    )

    OS = models.CharField(
        verbose_name=_("Operating system"),
        max_length=255,
    )

class dashboard(Probe):
    event = models.ManyToManyField(
        Event,
        verbose_name=_("Event"),
        help_text=_("List all the Event"),
    )
