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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(client_manager=user)
        self.fields['message'].queryset = Message.objects.filter(client_manager=user)


class MailingManagerForm(StyleFormMixin, ModelForm):
    """
    Форма редактирования рассылки менеджером
    """
    class Meta:
        model = Mailing
        fields = ['status',]
