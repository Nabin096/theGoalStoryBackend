# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-08 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SharedExperiences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogsmetadata',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blogsmetadata',
            name='publishingDate',
        ),
    ]
