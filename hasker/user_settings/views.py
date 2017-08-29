# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from signup.models import UserProfile
from .forms import SettingsForm


class UserSettingsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        form = SettingsForm(instance=user)
        try:
            profile = user.user_profile
            avatar = profile.avatar
        except UserProfile.DoesNotExist:
            avatar = None
        return render(request, 'settings.html', {'avatar': avatar,
                                                 'form': form})

    def post(self, request, *args, **kwargs):
        form = SettingsForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            try:
                profile = user.user_profile
            except UserProfile.DoesNotExist:
                profile = UserProfile(user=user)
            profile.avatar = form.cleaned_data.get('avatar')
            profile.save()
            return redirect('user_settings')
        return render(request, 'settings.html', {'form': form})
