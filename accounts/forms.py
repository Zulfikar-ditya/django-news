from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

from .models import User


class TextArea(forms.Textarea):
    input_type = 'text'


class DateInput(forms.DateInput):
    input_type = 'date'


# class PasswordInput(forms.PasswordInput):
    # input_type = 'password'


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
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
    
    def clean_password(self):
        return self.initial['password']


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'full_name',
            'address',
            'email',
            'gender',
            'date_of_birth',
        )
        widgets = {
            'date_of_birth': DateInput,
            'address': TextArea,
        }