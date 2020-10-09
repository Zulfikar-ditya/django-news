from django import forms
from .models import User


class TextArea(forms.Textarea):
    input_type = 'text'


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
# class RegisterForm()