# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 18:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pll', '0031_auto_20160402_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 13, 45, 16, 207751)),
        ),
        migrations.AlterField(
            model_name='voice',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 13, 45, 16, 209252)),
        ),
    ]