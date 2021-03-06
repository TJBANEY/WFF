# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-14 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0016_auto_20170813_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='stem_length_units',
        ),
        migrations.AlterField(
            model_name='plant',
            name='availability',
            field=models.CharField(choices=[('NA', '----'), ('SD', 'Seed'), ('PL', 'Plug'), ('PP', 'Potted Plant')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='plant',
            name='best_use',
            field=models.CharField(choices=[('NA', '---'), ('LA', 'Large Arrangement'), ('SA', 'Small Arrangement'), ('BF', 'Body Flower / Corsage'), ('LO', 'Landscape Only')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='plant',
            name='germination',
            field=models.CharField(choices=[('NA', '-----'), ('NL', 'Needs Light'), ('ND', 'Needs Darkness'), ('NA', 'Neither')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='plant',
            name='hardiness_zone',
            field=models.CharField(choices=[('NA', '--'), ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('3A', '3A'), ('3B', '3B'), ('4A', '4A'), ('4B', '4B'), ('5A', '5A'), ('5B', '5B'), ('6A', '6A'), ('6B', '6B'), ('7A', '7A'), ('7B', '7B'), ('8A', '8A'), ('8B', '8B'), ('9A', '9A'), ('9B', '9B'), ('10A', '10A'), ('10B', '10B'), ('11A', '11A'), ('11B', '11B'), ('12A', '12A'), ('12B', '12B'), ('13A', '13A'), ('13B', '13B')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='plant',
            name='lifespan',
            field=models.CharField(choices=[('NA', '------'), ('P', 'Perennial'), ('B', 'Biennial'), ('A', 'Annual')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('NA', '---'), ('HB', 'Herb'), ('SH', 'Shrub'), ('TR', 'Tree'), ('GR', 'Grass')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='plant',
            name='stem_length',
            field=models.FloatField(default=1, help_text='Always in centimeters'),
        ),
    ]
