# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField()),
                ('desc', models.TextField()),
                ('categories', models.TextField()),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]