# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.conf import settings

from .forms import AskQuestionForm, AnswerForm
from .models import Question, Tag, Answer


class QuestionList(ListView):
    """List of questions for index page."""
    template_name = 'index.html'
    model = Question
    context_object_name = 'questions'
    paginate_by = settings.QUESTIONS_PAGE_SIZE

    def get_ordering(self):
        order = self.request.GET.get('order', 'created')
        # TODO if field name does not exists
        return '-' + order

    def get_queryset(self):
        q = super(QuestionList, self).get_queryset()
        if 'tag' in self.kwargs:
            q = q.filter(tags__word=self.kwargs['tag'])
        return q.annotate(answer_count=Count('answers'))

    def get_context_data(self, **kwargs):
        ctx = super(QuestionList, self).get_context_data(**kwargs)
        ctx['order'] = self.request.GET.get('order', 'created')
        return ctx


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
            question = Question.ask_question(form)
            return redirect('question', slug=question.slug)
        return render(request, 'ask.html', {'form': form})


class QuestionView(ListView):
    template_name = 'question.html'
    model = Answer
    context_object_name = 'answers'
    paginate_by = settings.ANSWERS_PAGE_SIZE

    def get_ordering(self):
        return ['-correct', '-votes', '-created']

    def get_context_data(self, **kwargs):
        ctx = super(QuestionView, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        form = AnswerForm()
        ctx['question'] = question
        ctx['form'] = form
        return ctx

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        return Answer.objects.filter(question=question)

    @method_decorator(login_required)
    def post(self, request, *argc, **kwargs):
        slug = kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        form = AnswerForm(request.POST)
        if form.is_valid():
            Answer.post_answer(request.user, question, form)
        return redirect('question', slug=slug)


class AnswerCorrect(LoginRequiredMixin, View):
    http_method_names = ('get',)

    def get(self, request, *argc, **kwargs):
        answer_id = kwargs['id']
        answer = get_object_or_404(Answer, id=answer_id)
        question = answer.question
        if request.user == question.author:
            if question.correct == answer:
                question.correct = None
            else:
                question.correct = answer
            question.save()
        return redirect('question', slug=question.slug)
