from django.conf.urls import url, include
from rest_framework import routers
from .views import QuestionViewSet, TrendingList, TagViewSet, SearchList, AnswerViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet, base_name='questions')
router.register(r'answers', AnswerViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^trending/$', TrendingList.as_view()),
    url(r'^search/$', SearchList.as_view())
    #url(r'auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
]
