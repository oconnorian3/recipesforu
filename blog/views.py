from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

def home(request):
    return render(request, 'blog/home.html')