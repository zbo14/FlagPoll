# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pll', '0024_auto_20160327_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 27, 11, 21, 25, 957263)),
        ),
        migrations.AlterField(
            model_name='voice',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 27, 11, 21, 25, 961766)),
        ),
    ]