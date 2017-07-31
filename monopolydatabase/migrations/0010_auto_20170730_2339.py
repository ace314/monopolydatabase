# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 15:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monopolydatabase', '0009_auto_20170730_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='houses',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='land',
            name='land_type',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='land',
            name='land_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='bank_money',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='pocket_money',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='poisoned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='players_stock_list',
            name='stock_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_value',
            field=models.IntegerField(default=0),
        ),
    ]
