# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from qs.models import Answer, AnswerVotedUser, Question, QuestionVotedUser


def vote_question(request, *args, **kwargs):
    return process_vote(Question, QuestionVotedUser, ('question', 'user'), request, **kwargs)


def vote_answer(request, *args, **kwargs):
    return process_vote(Answer, AnswerVotedUser, ('answer', 'user'), request, **kwargs)


def is_can_vote(new_vote, saved_vote):
    return not new_vote == saved_vote


def process_vote(vote_subject, inter_table, inter_table_fields, request, **kwargs):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'error': 'Method not allowed.'}), content_type='application/json', status=405)
    if not request.user.is_authenticated:
        raise PermissionDenied()
    try:
        id = kwargs['id']
    except KeyError:
        return HttpResponse(json.dumps({'error': 'Bad request.'}), content_type='application/json', status=400)
    vote = request.POST['vote']
    if vote not in ['up', 'down']:
        return HttpResponse(json.dumps({'error': 'Bad request.'}), content_type='application/json', status=400)
    new_vote = 1 if vote == 'up' else -1
    subject = get_object_or_404(vote_subject, id=id)
    user = request.user
    try:
        kw = dict(zip(inter_table_fields, (subject, user)))
        subject_voted_user = inter_table.objects.get(**kw)
        saved_vote = subject_voted_user.result
    except inter_table.DoesNotExist:
        subject_voted_user = None
        saved_vote = 0
    if not is_can_vote(new_vote, saved_vote):
        return HttpResponse(json.dumps({'error': 'You already voted!'}), content_type='application/json', status=400)
    if not subject_voted_user:
        kw = dict(zip(inter_table_fields, (subject, user)))
        kw['result'] = new_vote
        subject_voted_user = inter_table(**kw)
        subject_voted_user.save()
    else:
        if new_vote + saved_vote == 0:
            subject_voted_user.delete()
        else:
            subject_voted_user.result = new_vote
            subject_voted_user.save()
    subject.votes += new_vote
    subject.save()
    return HttpResponse(json.dumps({'result': subject.votes}), content_type='application/json')
