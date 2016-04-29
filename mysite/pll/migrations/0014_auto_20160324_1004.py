# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 15:04
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pll', '0013_auto_20160324_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoter', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 24, 10, 4, 10, 483964)),
        ),
        migrations.AlterField(
            model_name='voice',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 24, 10, 4, 10, 488968)),
        ),
        migrations.AlterField(
            model_name='voice',
            name='upvotes',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='upvote',
            name='voice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pll.Voice'),
        ),
    ]