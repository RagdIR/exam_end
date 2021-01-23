from django import forms
from webapp.models import Users, Message


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['users']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}