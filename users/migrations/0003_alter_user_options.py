# Generated by Django 4.2 on 2024-06-15 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_new_email_user_new_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_active', 'Can block user')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
