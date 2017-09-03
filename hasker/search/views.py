# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
from django.db.models import Count, Q
from qs.models import Question


class SearchView(ListView):
    model = Question
    template_name = 'search.html'
    context_object_name = 'questions'
    paginate_by = settings.SEARCH_PAGE_SIZE

    def get_queryset(self):
        q = super(SearchView, self).get_queryset()
        if 'q' in self.request.GET:
            search_text = self.request.GET.get('q')
            q = q.filter(Q(title__icontains=search_text) |
                         Q(content__icontains=search_text))
        return q.order_by('-votes').annotate(answer_count=Count('answers'))
