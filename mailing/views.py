from random import sample

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from blog.models import Post
from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Mailing, Client, Message, Attempt


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse_lazy('mailing:mailing', args=[self.kwargs.get('pk')])


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('mailing:mailing', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('mailing:client', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('mailing:message', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class HomePage(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["mailing_count"] = Mailing.objects.all().count()
        context_data["active_mailing_count"] = Mailing.objects.filter(status__in=['CREATED', 'IN_PROGRESS']).count()
        context_data["unique_clients_count"] = Client.objects.all().distinct('email').count()
        all_posts = list(Post.objects.all())
        context_data['random_posts'] = sample(all_posts, min(len(all_posts), 3))
        return context_data


class AttemptListView(ListView):
    model = Attempt
