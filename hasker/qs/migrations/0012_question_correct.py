# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qs', '0011_auto_20170825_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answered_question', to='qs.Answer'),
        ),
    ]