# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0003_probe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='description',
            field=models.TextField(help_text='Description of the probe', max_length=1200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='probe',
            name='domain',
            field=models.CharField(help_text='Domain the probe will be attached to', max_length=200, verbose_name='Domain'),
        ),
        migrations.AlterField(
            model_name='probe',
            name='is_enabled',
            field=models.BooleanField(default=False, help_text='Check the box if you want the probe to be enabled', verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='probe',
            name='sensors',
            field=models.ManyToManyField(help_text='Sensors to be used by the probe (Use CTRL + Left Mouse Button to select)', to='probe_dispatcher.Sensor', blank=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='code',
            field=models.TextField(default=b'', help_text='Code in the Cornipickle language', verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(help_text='Name of the sensor', max_length=200, verbose_name='Name'),
        ),
    ]
