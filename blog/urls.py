from . import views
from .views import create_post
from .views import edit_post
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]