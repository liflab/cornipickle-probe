# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('description', models.TextField(max_length=1200, verbose_name='Description')),
                ('domain', models.CharField(max_length=200, verbose_name='Domain')),
                ('hash', models.CharField(verbose_name='Hash', max_length=40, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('code', models.TextField(default=b'', verbose_name=b'Code')),
            ],
        ),
        migrations.AddField(
            model_name='probe',
            name='sensors',
            field=models.ManyToManyField(to='probe_dispatcher.Sensor'),
        ),
        migrations.AddField(
            model_name='probe',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, help_text='Owner of the probe'),
        ),
    ]
