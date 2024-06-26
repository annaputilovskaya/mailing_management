from django.forms import ModelForm

from blog.models import Post
from users.forms import StyleFormMixin


class PostForm(StyleFormMixin, ModelForm):
    """
    Форма создания статьи
    """
    class Meta:
        model = Post
        exclude = ['slug', 'views_count']
