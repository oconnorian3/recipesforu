from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'author', 'status', 'image',)
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

    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file', 'id': 'image-input'})
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        post = super().save(commit=False)
        image = self.cleaned_data.get('image')
        if image:
            post.image = image
        if commit:
            post.save()
        return post


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'status', 'image',]
    
    image = forms.ImageField(required=False)