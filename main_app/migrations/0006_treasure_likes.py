# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20170606_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]