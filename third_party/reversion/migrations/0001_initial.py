# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-08-20 01:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_slug', models.CharField(db_index=True, default='default', max_length=191)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The date and time this revision was created.', verbose_name='date created')),
                ('comment', models.TextField(blank=True, help_text='A text comment on this revision.', verbose_name='comment')),
                ('user', models.ForeignKey(blank=True, help_text='The user who created this revision.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.TextField(help_text='Primary key of the model under version control.')),
                ('object_id_int', models.IntegerField(blank=True, db_index=True, help_text="An indexed, integer version of the stored model's primary key, used for faster lookups.", null=True)),
                ('format', models.CharField(help_text='The serialization format used by this model.', max_length=255)),
                ('serialized_data', models.TextField(help_text='The serialized form of this version of the model.')),
                ('object_repr', models.TextField(help_text='A string representation of the object.')),
                ('content_type', models.ForeignKey(help_text='Content type of the model under version control.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('revision', models.ForeignKey(help_text='The revision that contains this version.', on_delete=django.db.models.deletion.CASCADE, to='reversion.Revision')),
            ],
        ),
    ]
