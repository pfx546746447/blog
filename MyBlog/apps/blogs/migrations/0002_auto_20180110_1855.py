# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-10 10:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 10, 55, 50, 706000, tzinfo=utc), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 10, 55, 50, 706000, tzinfo=utc), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
