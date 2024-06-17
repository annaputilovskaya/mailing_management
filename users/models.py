from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)
    new_email = models.EmailField(
        verbose_name='Email', **NULLABLE,
        help_text='Для подтверждения изменения почты необходимо пройти по ссылке, направленной на email')
    new_token = models.CharField(max_length=100, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [('set_active', 'Can block user'),]
