from django import forms
from webapp.models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['users']