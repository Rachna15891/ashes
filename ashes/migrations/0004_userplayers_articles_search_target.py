# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashes', '0003_userplayers_search_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='userplayers',
            name='articles_search_target',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
