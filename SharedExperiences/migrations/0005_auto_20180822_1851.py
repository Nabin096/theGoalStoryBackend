# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-22 13:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SharedExperiences', '0004_auto_20180822_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsmetadata',
            name='title',
            field=models.CharField(default='Lorem ipsum set amore', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogsmetadata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 18, 51, 28, 917006)),
        ),
    ]
