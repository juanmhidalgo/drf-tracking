# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_tracking', '0004_add_verbose_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequestlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]