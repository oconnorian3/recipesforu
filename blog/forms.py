from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post
from django import forms
from .models import Contact
from .models import Comment


# Post Foem

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'status', 'author', 'featured_image',)
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'title': 'Post Title',
            'slug': 'Slug',
            'content': 'Body',
            'status': 'Status',
            'author': 'Author',
            'featured_image': 'Image',
        }
        help_texts = {
            'featured_image': 'Please upload an image for your post',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        if user:
            self.initial['author'] = user.pk
            self.fields['author'].widget = forms.HiddenInput()

    def save(self, commit=True):
        post = super().save(commit=False)
        if 'author' in self.initial:
            post.author_id = self.initial['author']
        if commit:
            post.save()
        return post


# Edit Post Form


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'status', 'featured_image',]
        widgets = {
            'content': SummernoteWidget(),
        }

        labels = {
            'title': 'Post Title',
            'slug': 'Slug',
            'content': 'Body',
            'author': 'Author',
            'status': 'Status',
            'featured_image': 'Image',
        }

# Contact Form


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        labels = {
            'Name': 'Name',
            'Email': 'Email',
            'Subject': 'Subject',
            'Message': 'Message',
        }    

# Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)