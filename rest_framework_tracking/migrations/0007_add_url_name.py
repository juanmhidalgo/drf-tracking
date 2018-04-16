# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rest_framework_tracking", "0006_auto_20180315_1442"),
    ]

    operations = [
        migrations.AddField(
            'APIRequestLog',
            'url_name',
            models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
