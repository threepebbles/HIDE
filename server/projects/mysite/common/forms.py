from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

class LoginSuccessForm(UserCreationForm):
    login_state = forms.Field(label="login_state")