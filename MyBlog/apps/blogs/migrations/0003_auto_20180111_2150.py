# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-11 13:50
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20180110_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=DjangoUeditor.models.UEditorField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
