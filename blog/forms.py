from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'author', 'status', 'featured_image',)
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'title': '',
            'slug': '',
            'content': '',
            'author': '',
            'status': '',
            'image': '',
        }
        help_texts = {
            'image': 'Please upload an image for your post',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'status', 'featured_image',]
        widgets = {
            'content': SummernoteWidget(),
        }
    