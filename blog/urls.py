from . import views
from .views import create_post
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/',views.create_post, name='create_post'),
]