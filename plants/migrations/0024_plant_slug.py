# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-20 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0023_auto_20170820_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
