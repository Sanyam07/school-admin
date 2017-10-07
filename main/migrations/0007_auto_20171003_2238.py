# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 22:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171003_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='excutive_religion',
            field=models.CharField(choices=[('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Traditional', 'Traditional')], default=datetime.datetime(2017, 10, 3, 22, 38, 27, 432590, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teachers_religion',
            field=models.CharField(choices=[('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Traditional', 'Traditional')], default=datetime.datetime(2017, 10, 3, 22, 38, 36, 648069, tzinfo=utc), max_length=17),
            preserve_default=False,
        ),
    ]
