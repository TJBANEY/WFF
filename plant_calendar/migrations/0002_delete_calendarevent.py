# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-17 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_calendar', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='calendarEvent',
        ),
    ]
