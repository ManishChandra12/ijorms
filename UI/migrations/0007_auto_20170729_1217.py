# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0006_auto_20170729_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='appliers',
        ),
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2017, 8, 5, 12, 17, 57, 694307)),
        ),
    ]
