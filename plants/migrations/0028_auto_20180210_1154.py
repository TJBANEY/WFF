# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-02-10 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0027_auto_20170919_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plant',
            options={'ordering': ('botanical_name',), 'verbose_name': 'Plant', 'verbose_name_plural': 'Plants'},
        ),
    ]
