# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db.models import Count, Q
from rest_framework import viewsets, generics
from rest_framework import pagination
from qs.models import Question, Answer, Tag
from .serializers import QuestionSerializer, TagSerializer, AnswerSerializer


class QuestionPagination(pagination.PageNumberPagination):
    page_size = settings.QUESTIONS_PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = 10


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination

    # TODO order
    def get_queryset(self):
        q = Question.objects.all()
        return q.annotate(answer_count=Count('answers'))


class TrendingList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.order_by('-votes')[:20]


class SearchList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination

    def get_queryset(self):
        if 'q' in self.request.GET:
            search_text = self.request.GET.get('q')
            q = Question.objects.filter(Q(title__icontains=search_text) |
                                        Q(content__icontains=search_text))
            return q.order_by('-votes').annotate(answer_count=Count('answers'))
        else:
            return Question.objects.none()


class AnswerPagination(pagination.PageNumberPagination):
    page_size = settings.ANSWERS_PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = 20


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    pagination_class = AnswerPagination
    queryset = Answer.objects.all()


class TagPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    pagination_class = TagPagination
    queryset = Tag.objects.all()
