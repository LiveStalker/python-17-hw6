# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
