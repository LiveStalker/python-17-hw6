# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qs', '0010_auto_20170825_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]