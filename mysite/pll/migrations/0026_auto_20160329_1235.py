# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 17:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pll', '0025_auto_20160327_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 29, 12, 35, 27, 933559)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='result',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='poll',
            name='tag',
            field=models.CharField(choices=[('Community Development', 'Community Development'), ('Education', 'Education'), ('Sustainability', 'Sustainability'), ('Facilities & Geographic Boundaries', 'Facilities & Geographic Boundaries'), ('Health & Human Services', 'Health & Human Services'), ('Historic Preservation', 'Historic Preservation'), ('Parks & Rec', 'Parks & Rec'), ('Public Safety', 'Public Safety'), ('Sanitation', 'Sanitation'), ('Transportation', 'Transportation')], default='no tag', max_length=30),
        ),
        migrations.AlterField(
            model_name='updownvote',
            name='voice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pll.Voice'),
        ),
        migrations.AlterField(
            model_name='voice',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 29, 12, 35, 27, 933559)),
        ),
    ]
