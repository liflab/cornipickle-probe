# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0007_auto_20161007_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probe',
            name='is_valid',
        ),
    ]
