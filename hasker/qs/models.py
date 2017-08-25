# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    word = models.CharField(max_length=50, blank=False, null=False)


class QuestionVotedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    result = models.SmallIntegerField()


class Question(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, related_name='questions')
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='questions')
    votes = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True)
    voters = models.ManyToManyField(User, through='QuestionVotedUser', related_name='voted_questions')

    @models.permalink
    def get_absolute_url(self):
        return 'question', (self.slug,)

    @property
    def is_correct_answered(self):
        return self.answers.filter(correct=True).count()


class AnswerVotedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    result = models.SmallIntegerField()


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, related_name='answers')
    created = models.DateTimeField(auto_now_add=True)
    correct = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, through='AnswerVotedUser', related_name='voted_answers')

    @models.permalink
    def get_correct_url(self):
        return 'answer_correct', (self.id,)
