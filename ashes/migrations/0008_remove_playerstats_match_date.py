# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ashes', '0007_playerstats_match_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerstats',
            name='match_date',
        ),
    ]
