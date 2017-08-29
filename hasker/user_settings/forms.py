from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class ReadonlyCharField(forms.CharField):
    readonly = True

    def __init__(self, *args, **kwargs):
        super(ReadonlyCharField, self).__init__(*args, **kwargs)


class SettingsForm(ModelForm):
    username = ReadonlyCharField()
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')
