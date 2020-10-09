from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class TextArea(forms.Textarea):
    input_type = 'text'


class DateInput(forms.DateInput):
    input_type = 'date'


class UserAdminCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'full_name',
            'phone',
            'address',
            'email',
            'avatar',
            'gender',
            'date_of_birth',
            'username',
            'password',
            'is_superuser',
            'is_reporter',
            'is_staff',
            'is_active',
        )
        widgets = {
            'address': TextArea,
        }

class UserAdminChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'full_name',
            'phone',
            'address',
            'email',
            'avatar',
            'gender',
            'date_of_birth',
            'username',
            'password',
            'is_superuser',
            'is_reporter',
            'is_staff',
            'is_active',
        )


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'full_name',
            'phone',
            'address',
            'email',
            'avatar',
            'gender',
            'date_of_birth',
            'username',
            'password',
        )
        widgets = {
            'date_of_birth': DateInput,
            'address': TextArea,
        }