# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashes', '0008_remove_playerstats_match_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermatchdata',
            name='caa',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='playermatchdata',
            name='last_bat_impact',
            field=models.FloatField(default=0, null=True),
        ),
    ]