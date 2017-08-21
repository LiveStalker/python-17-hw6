"""hasker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from signup.forms import LoginForm
from signup import views as signup_views
from qs import views as qs_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', qs_views.QuestionList.as_view(), name='index'),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'form_class': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup_views.SignUpView.as_view(), name='signup'),

    url(r'ask/$', qs_views.AskQuestionView.as_view(), name='ask'),
    url(r'question/(?P<slug>[-\w]+)/$', qs_views.QuestionView.as_view(), name='question'),
    url(r'answer_correct/(?P<id>\d+)/$', qs_views.AnswerCorrect.as_view(), name='answer_correct'),
]
