# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monopolydatabase', '0007_land'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='poisoned',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
