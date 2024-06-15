from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(PostListView.as_view()), name='post_list'),
    path('view/<slug:slug>/', cache_page(60)(PostDetailView.as_view()), name='post'),
    path('blog/create/', PostCreateView.as_view(), name='post_create'),
    path('blog/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('blog/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
