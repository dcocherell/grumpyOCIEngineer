from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg shadow',
                'placeholder': 'Enter post title',
                'color': 'black'
            }),
            'author': forms.Select(attrs={
                'class': 'form-select form-select-lg shadow',
                'color': 'black'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control shadow',
                'rows': 5,
                'placeholder': 'Write your post here',
                'color': 'black'
            }),
        }

        # ensure that each widget field is visible on the background
        