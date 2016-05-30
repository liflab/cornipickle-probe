# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('probe_dispatcher', '0002_remove_probe_script_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='tags_and_attributes',
            field=jsonfield.fields.JSONField(default={b'tagnames': b'', b'attributes': b''}, editable=False),
        ),
    ]
