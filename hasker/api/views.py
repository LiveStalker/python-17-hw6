# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db.models import Count
from rest_framework import viewsets, generics
from rest_framework import pagination
from qs.models import Question, Answer, Tag
from .serializers import QuestionSerializer


class QuestionPagination(pagination.PageNumberPagination):
    page_size = settings.QUESTIONS_PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = 10


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination

    # TODO order
    # TODO search
    def get_queryset(self):
        q = Question.objects.all()
        return q.annotate(answer_count=Count('answers'))


class TrendingList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.order_by('-votes')[:20]
