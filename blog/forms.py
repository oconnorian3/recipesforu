from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post
from .models import ContactForm


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

## Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'subject': 'Subject',
            'message': 'Message'
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Subject'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message'})
