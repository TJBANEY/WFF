# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-17 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_auto_20170716_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantevent',
            name='color',
            field=models.CharField(blank=True, default='1bc974', help_text='This will be the color of the event on the dashboard calendar', max_length=10, null=True),
        ),
    ]