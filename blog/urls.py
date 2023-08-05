from django.urls import path
from .views import BlogListView, BlogDetailView, NewPost, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'), 
    path('post/new/', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView, name='home'),
]