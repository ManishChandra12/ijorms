# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 07:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0022_auto_20170805_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 7, 34, 59, 521160, tzinfo=utc)),
        ),
    ]
