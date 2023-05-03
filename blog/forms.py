from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'author', 'status', 'image',)
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}),
        'author': forms.Select(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
        'image': forms.FileInput(attrs={'class': 'form-control-file'})
    }
    image = forms.ImageField(required=False)

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'status', 'image',]
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}),
        'author': forms.Select(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
        'image': forms.FileInput(attrs={'class': 'form-control-file'})
    }

    image = forms.ImageField(required=False)