# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 19:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pll', '0032_auto_20160402_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 14, 23, 8, 836013)),
        ),
        migrations.AlterField(
            model_name='voice',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 14, 23, 8, 837514)),
        ),
    ]
