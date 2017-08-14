# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AskQuestionForm
from .models import Question, Tag


class AskQuestionView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    # TODO remove query string ?next

    def get(self, request, *args, **kwargs):
        form = AskQuestionForm()
        return render(request, 'ask.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            question = Question()
            question.title = form.cleaned_data.get('title')
            question.content = form.cleaned_data.get('content')
            question.author = request.user
            question.save()
            for word in form.cleaned_data.get('tags'):
                #TODO if tag exist
                tag = Tag(word=word)
                tag.save()
                question.tags.add(tag)
            question.save()
            return redirect('index')
        return render(request, 'ask.html', {'form': form})
