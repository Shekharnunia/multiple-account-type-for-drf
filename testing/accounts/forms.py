from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  SchoolProfile


class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.is_teacher = True

        if commit:
            user.save()

        return user