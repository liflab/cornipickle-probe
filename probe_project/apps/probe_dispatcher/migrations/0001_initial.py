# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the probe', max_length=255, verbose_name='Name')),
                ('description', models.TextField(help_text='Description of the probe', max_length=1200, verbose_name='Description')),
                ('domain', models.CharField(help_text='Domain the probe will be attached to', max_length=200, verbose_name='Domain')),
                ('hash', models.CharField(verbose_name='Hash', max_length=40, editable=False)),
                ('is_enabled', models.BooleanField(default=False, help_text='Check the box if you want the probe to be enabled', verbose_name='Enabled')),
                ('pid', models.IntegerField(verbose_name=b'pid', null=True, editable=False, blank=True)),
                ('tags_and_attributes', jsonfield.fields.JSONField(default={}, editable=False)),
                ('script_url', models.CharField(help_text='The URL of the script for this probe', max_length=200, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the sensor', max_length=200, verbose_name='Name')),
                ('code', models.TextField(default=b'', help_text='Code in the Cornipickle language', verbose_name='Code')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, help_text='Owner of the sensor')),
            ],
        ),
        migrations.AddField(
            model_name='probe',
            name='sensors',
            field=models.ManyToManyField(help_text='Sensors to be used by the probe (Use CTRL + Left Mouse Button to select)', to='probe_dispatcher.Sensor', blank=True),
        ),
        migrations.AddField(
            model_name='probe',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, help_text='Owner of the probe'),
        ),
    ]
