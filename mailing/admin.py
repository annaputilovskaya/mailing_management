from django.contrib import admin

from mailing.models import Client, Mailing, Message, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comments')
    list_filter = ('name', 'email', 'comments')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'text')
    list_filter = ('subject',)
    search_fields = ('subject', 'text',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_mailing', 'periodicity', 'status', 'message')
    list_filter = ('start_mailing', 'periodicity', 'status', 'message')


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_attempt', 'status', 'response', 'mailing')
    list_filter = ('last_attempt', 'status', 'response', 'mailing')
