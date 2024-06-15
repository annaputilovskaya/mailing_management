from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    """
    Контроллер для отображения списка статей
    """
    model = Post

    def get_queryset(self):
        return super().get_queryset().order_by('-published_at')


class PostDetailView(DetailView):
    """
    Контроллер для отображения детальной информации о статье
    """
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Контроллер для создания новой статьи
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    permission_required = 'blog.add_post'

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Контроллер для редактирования статьи
    """
    model = Post
    fields = '__all__'
    permission_required = 'blog.change_post'

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', args=[self.kwargs.get('slug')])


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Контроллер для удаления статьи
    """
    model = Post
    success_url = reverse_lazy('blog:post_list')
    permission_required = 'blog.delete_post'
