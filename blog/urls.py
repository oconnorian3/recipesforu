from . import views
from .views import create_post
from .views import edit_post
from .views import delete_post
from django.urls import path
from .views import contact_view
from django.core.exceptions import PermissionDenied

def permission_denied_view(request, exception=None):
    return TemplateView.as_view(template_name='403.html')(request)

# Add custom handlers for exceptions
handler403 = permission_denied_view    

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('contact/', contact_view, name='contact'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]