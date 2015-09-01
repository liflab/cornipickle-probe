# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0004_auto_20150722_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='probe',
            name='tags_and_attributes',
            field=jsonfield.fields.JSONField(default={}, editable=False),
        ),
    ]
