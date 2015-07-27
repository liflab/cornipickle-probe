# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0002_auto_20150708_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='probe',
            name='pid',
            field=models.IntegerField(verbose_name=b'pid', null=True, editable=False, blank=True),
        ),
    ]
