# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-12 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='sex',
            field=models.CharField(choices=[('man', '\u7537'), ('woman', '\u5973')], max_length=5, verbose_name='\u6027\u522b'),
        ),
    ]
