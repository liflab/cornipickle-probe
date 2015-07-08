# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0002_probe_is_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='is_enabled',
            field=models.BooleanField(default=False, verbose_name=b'Enabled'),
        ),
    ]
