# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0005_auto_20170727_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillScore', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('workExpScore', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('educationScore', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('certificationScore', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UI.Applicant')),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2017, 8, 5, 12, 17, 10, 899014)),
        ),
        migrations.AddField(
            model_name='jobapplicant',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UI.Job'),
        ),
    ]
