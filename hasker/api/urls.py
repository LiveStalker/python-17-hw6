from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from .views import QuestionViewSet, TrendingList, TagViewSet, \
    SearchList, AnswerViewSet, QuestionAnswersList

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet, base_name='questions')
router.register(r'answers', AnswerViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^trending/$', TrendingList.as_view()),
    url(r'^search/$', SearchList.as_view()),
    url(r'^questions/(?P<question_id>\d+)/answers/$', QuestionAnswersList.as_view()),
    url(r'^auth/login/', obtain_jwt_token, name='api-auth'),
]
