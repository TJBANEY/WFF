# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-20 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0024_plant_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='account.Account'),
        ),
    ]
