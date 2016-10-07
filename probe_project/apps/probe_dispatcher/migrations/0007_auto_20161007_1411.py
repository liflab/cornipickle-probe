# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0006_sensor_isvalid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='isvalid',
            new_name='is_valid',
        ),
        migrations.AddField(
            model_name='probe',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='Valid', editable=False),
        ),
    ]
