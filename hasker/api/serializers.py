from rest_framework import serializers
from qs.models import Question, Answer, Tag


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'word',)


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    votes = serializers.IntegerField(read_only=True)
    answer_count = serializers.IntegerField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'author', 'created', 'votes', 'answer_count', 'tags')


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    votes = serializers.IntegerField(read_only=True)
    correct = serializers.BooleanField(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'question', 'content', 'author', 'created', 'correct', 'votes')
