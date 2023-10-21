from django.forms import CharField, EmailField, Form
from django.contrib.auth import models as auth_models
from django.contrib.auth import forms as auth_forms

class RegistrationForm(auth_forms.UserCreationForm):
    user_name = CharField(max_length=40, required=True)
    user_surname = CharField(max_length=40, required=True)
    email = EmailField(max_length=50, required=True)

    class Meta:
        model = auth_models.User
        fields = ['user_name', 'user_surname', 'email', 'password']
