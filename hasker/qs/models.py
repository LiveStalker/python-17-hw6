# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, related_name='questions')
    created = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='questions')


class Answer(models.Model):
    pass


class Tag(models.Model):
    word = models.CharField(max_length=50, blank=False, null=False)
