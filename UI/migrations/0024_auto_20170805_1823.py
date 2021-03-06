# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 12:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0023_auto_20170805_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 12, 38, 47, 804820, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='certificationScore',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='educationScore',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='skillScore',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='workExpScore',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=7),
        ),
    ]
