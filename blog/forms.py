from django import forms
from .models import Post,Script

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        model = Script
        fields = ("__all__")