from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg shadow',
                'placeholder': 'Enter post title',
                'color': 'black'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control shadow',
                'rows': 5,
                'placeholder': 'Write your post here',
                'color': 'black'
            }),
            'category': forms.Select(choices=choices, attrs={
                'class': 'form-control shadow',
                'color': 'black'
            })
        }