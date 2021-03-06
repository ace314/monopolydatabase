# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 15:10
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monopolydatabase', '0008_auto_20170726_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='land_value',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='random_risefall_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=0, size=30),
            preserve_default=False,
        ),
    ]
