from django.forms import ModelForm

from mailing.models import Client, Message, Mailing
from users.forms import StyleFormMixin


class ClientForm(StyleFormMixin, ModelForm):
    """
    Форма для редактирования клиента
    """
    class Meta:
        model = Client
        fields = ['name', 'email', 'comments']


class MessageForm(StyleFormMixin, ModelForm):
    """
    Форма для редактирования сообщения
    """
    class Meta:
        model = Message
        fields = ['subject', 'text']


class MailingForm(StyleFormMixin, ModelForm):
    """
    Форма для редактирования рассылки
    """
    class Meta:
        model = Mailing
        fields = ['start_mailing', 'end_mailing', 'periodicity', 'status', 'message', 'clients']


class MailingManagerForm(StyleFormMixin, ModelForm):
    """
    Форма редактирования рассылки менеджером
    """
    class Meta:
        model = Mailing
        fields = ['status',]
