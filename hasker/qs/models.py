# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils.text import slugify


class Tag(models.Model):
    word = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.word

    def __unicode__(self):
        return self.word


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

    @staticmethod
    def ask_question(user, form):
        with transaction.atomic():
            question = Question()
            question.title = form.cleaned_data.get('title')
            question.content = form.cleaned_data.get('content')
            question.author = user
            question.slug = slugify(question.title)
            question.save()
            for word in form.cleaned_data.get('tags'):
                try:
                    tag = Tag.objects.get(word=word)
                except Tag.DoesNotExist:
                    tag = Tag(word=word)
                    tag.save()
                question.tags.add(tag)
            question.save()
            return question

    @models.permalink
    def get_absolute_url(self):
        return 'question', (self.slug,)

    @property
    def is_correct_answered(self):
        return self.answers.filter(correct=True).count()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title[:50]


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

    @staticmethod
    def post_answer(user, question, form):
        with transaction.atomic():
            answer = form.save(commit=False)
            answer.author = user
            answer.question = question
            answer.save()
            return answer

    @models.permalink
    def get_correct_url(self):
        return 'answer_correct', (self.id,)
