# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0005_auto_20160613_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='isvalid',
            field=models.BooleanField(default=False, help_text='Code validity', verbose_name='Code validity', editable=False),
        ),
    ]
