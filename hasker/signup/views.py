# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import UserProfile


def index(request):
    return render(request, 'index.html')


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # TODO transaction
            user = form.save()
            profile = UserProfile(user=user)
            profile.avatar = form.cleaned_data.get('avatar')
            profile.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('index')
        return render(request, 'signup.html', {'form': form})
