# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-20 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170612_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='zip',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]