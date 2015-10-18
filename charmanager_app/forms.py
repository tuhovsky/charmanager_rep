from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import UserCharacter


class UserCharacterForm(ModelForm):

    class Meta:
        model = UserCharacter
        fields = ['username', 'nickname',
                  'gender', 'level', 'specialization', 'skills', ]


class UserCharacterChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(UserCharacterChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = UserCharacter
        fields = ['username', 'nickname',
                  'gender', 'level', 'specialization', 'skills', ]


class UserCharacterCreationForm(UserCreationForm):

    class Meta:
        model = UserCharacter
        fields = ['username', 'email']


class FilterForm(ModelForm):

    class Meta:
        model = UserCharacter
        fields = ('specialization', 'gender', )
