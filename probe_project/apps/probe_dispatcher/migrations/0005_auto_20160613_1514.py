# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0004_auto_20160525_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='sensors',
            field=models.ManyToManyField(help_text='Sensors to be used by the probe (Use CTRL + Left Mouse Button to select)', to='probe_dispatcher.Sensor', verbose_name='Sensor', blank=True),
        ),
    ]
