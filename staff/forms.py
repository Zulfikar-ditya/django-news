from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User
from accounts.forms import TextArea, DateInput
from home.models import Category


class AddReporterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'full_name',
            'phone',
            'address',
            'avatar',
            'gender',
            'date_of_birth',
        ]
        widgets = {
            'date_of_birth': DateInput,
            'address': TextArea,
        }


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = (
            'name',
            'img',
            'new',
            'trending',
        )
