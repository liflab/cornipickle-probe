# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0005_auto_20160613_1514'),
        ('dashboards', '0002_datum_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='datum',
            name='OS',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datum',
            name='httpReferer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datum',
            name='httpUserAgent',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datum',
            name='language',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datum',
            name='probeId',
            field=models.ForeignKey(default=1, to='probe_dispatcher.Probe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datum',
            name='slug',
            field=models.SlugField(default=11),
            preserve_default=False,
        ),
    ]
