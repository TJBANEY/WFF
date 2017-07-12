# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-17 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('PT', 'Plant Seeds'), ('MV', 'Move Plants'), ('PR', 'Prune Plants'), ('HV', 'Harvest'), ('OT', 'Other')], max_length=255)),
                ('name', models.CharField(help_text='e.g. Plant seeds, Move to larger pot, etc.', max_length=255)),
                ('event_start', models.DateTimeField(blank=True, null=True)),
                ('event_end', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.Plant')),
            ],
        ),
    ]