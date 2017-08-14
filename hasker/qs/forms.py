from django import forms
from .models import Question, Tag


class TagsField(forms.CharField):
    def to_python(self, value):
        tags = [el.strip() for el in value.split(',')]
        return tags


class AskQuestionForm(forms.ModelForm):
    tags = TagsField(max_length=200)

    class Meta:
        model = Question
        fields = ('title', 'content', 'tags')
