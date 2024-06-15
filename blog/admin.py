from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'published_at', 'views_count')
    list_filter = ('published_at', 'title')
    verbose_name = 'Статьи'
