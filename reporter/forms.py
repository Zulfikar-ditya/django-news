from django import forms

from home.models import Blog


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = (
            'title',
            'image',
            'content',
        )
