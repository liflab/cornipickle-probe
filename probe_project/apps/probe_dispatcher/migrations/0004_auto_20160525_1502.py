# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0003_auto_20160520_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probe',
            name='tags_and_attributes',
        ),
        migrations.AddField(
            model_name='probe',
            name='tags_attributes_interpreter',
            field=jsonfield.fields.JSONField(default={b'tagnames': b'', b'attributes': b'', b'interpreter': b''}, editable=False),
        ),
    ]
