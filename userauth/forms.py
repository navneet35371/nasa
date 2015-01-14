from django.forms import ModelForm
from django import forms
from userauth.models import UserProfile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [('website')]