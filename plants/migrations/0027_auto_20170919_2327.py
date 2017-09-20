# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-20 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0026_planttask'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planttask',
            options={'ordering': ('create_date',), 'verbose_name': 'Plant Task', 'verbose_name_plural': 'Plant Tasks'},
        ),
        migrations.AlterField(
            model_name='planttask',
            name='user_plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='plants.UserPlant'),
        ),
    ]
