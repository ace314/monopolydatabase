# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 16:00
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monopolydatabase', '0010_auto_20170730_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='random_risefall_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=30),
        ),
    ]