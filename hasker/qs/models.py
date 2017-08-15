# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    word = models.CharField(max_length=50, blank=False, null=False)


class Question(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, related_name='questions')
    created = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='questions')
    votes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

    @models.permalink
    def get_absolute_url(self):
        return 'question', (self.slug,)

    @property
    def answer_count(self):
        return self.answers.count()


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, related_name='answers')
    created = models.DateTimeField(default=timezone.now)
    correct = models.BooleanField(default=False)
