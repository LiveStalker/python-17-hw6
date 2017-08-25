# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponseBadRequest, HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from qs.models import Answer, AnswerVotedUser


def vote_question(request, *args, **kwargs):
    pass


def vote_answer(request, *args, **kwargs):
    if request.method != 'POST':
        # TODO return error
        pass
    if not request.user.is_authenticated:
        raise PermissionDenied()
    # TODO if key does not exists
    id = kwargs['id']
    vote = request.POST['vote']
    if vote not in ['up', 'down']:
        # TODO return error
        pass
    new_vote = 1 if vote == 'up' else -1
    answer = get_object_or_404(Answer, id=id)
    user = request.user
    try:
        answer_voted_user = AnswerVotedUser.objects.get(user=user, answer=answer)
        saved_vote = answer_voted_user.result
    except AnswerVotedUser.DoesNotExist:
        answer_voted_user = None
        saved_vote = 0
    if not is_can_vote(new_vote, saved_vote):
        return HttpResponse(json.dumps({'error': 'You already voted!'}), content_type='application/json', status=400)
    if not answer_voted_user:
        answer_voted_user = AnswerVotedUser(answer=answer, user=user, result=new_vote)
        answer_voted_user.save()
    else:
        if new_vote + saved_vote == 0:
            answer_voted_user.delete()
        else:
            answer_voted_user.result = new_vote
            answer_voted_user.save()
    answer.votes += new_vote
    answer.save()
    return HttpResponse(json.dumps({'result': answer.votes}), content_type='application/json')


def is_can_vote(new_vote, saved_vote):
    return not new_vote == saved_vote


def vote_operation(answer, user, new_vote, saved_vote):
    pass
