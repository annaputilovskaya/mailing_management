from django.contrib import admin

from mailing.models import Client, Mailing, Message, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comments')
    list_filter = ('name', 'email', 'comments')
    verbose_name = 'Клиенты'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'text')
    list_filter = ('subject',)
    search_fields = ('subject', 'text',)
    verbose_name = 'Сообщения'


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_mailing', 'periodicity', 'status', 'message')
    list_filter = ('start_mailing', 'periodicity', 'status', 'message')
    verbose_name = 'Рассылки'


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempt_date', 'status', 'response', 'mailing')
    list_filter = ('attempt_date', 'status', 'response', 'mailing')
    verbose_name = 'Попытки'
