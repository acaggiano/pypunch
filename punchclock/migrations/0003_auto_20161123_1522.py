# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punchclock', '0002_auto_20161116_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='time_end',
            field=models.DateTimeField(blank=True),
        ),
    ]
