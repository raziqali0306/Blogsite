from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta :
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }

class UpdateUserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ['username']
        help_texts = {
            'username': None,
        }



