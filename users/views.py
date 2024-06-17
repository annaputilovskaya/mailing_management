import secrets

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserCreateView(CreateView):
    """
    Контроллер регистрации пользователя
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save(update_fields=['token', 'is_active'])
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Здравствуйте. Для подтверждения адреса электронной почты, пожалуйста, перейдите по ссылке {url}. '
                    f'Служба поддержки Mailing Management.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """
    Проверят подлинность электронной почты
    """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    """
    Контроллер редактирования профиля пользователем
    """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = self.get_object()
        if user.email != form.cleaned_data['new_email']:
            user.new_email = form.cleaned_data['new_email']
            token = secrets.token_hex(16)
            user.new_token = token
            user.is_active = False
            user.save()
            host = self.request.get_host()
            url = f'http://{host}/users/change_email/{token}/'
            send_mail(
                subject='Подтверждение почты',
                message=f'Здравствуйте. Для подтверждения адреса электронной почты, '
                        f'пожалуйста, перейдите по ссылке {url}. Служба поддержки Mailing Management.',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.new_email],
            )
            return redirect(reverse('users:login'))
        user.save()
        return super().form_valid(form)


def change_email(request, token):
    """
    Изменяет электронную почту пользователя
    """
    user = get_object_or_404(User, new_token=token)
    user.email = user.new_email
    user.token = user.new_token
    user.new_token = ''
    user.is_active = True
    user.save()
    return redirect('users:profile')


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Контроллер списка пользователей
    """
    model = User
    permission_required = 'users.view_user'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            queryset = queryset.exclude(is_superuser=True)
        elif self.request.user.has_perm('users.view_user'):
            email = self.request.user.email
            queryset = queryset.exclude(email=email).exclude(is_superuser=True)
        return queryset


class UserDeleteView(UserPassesTestMixin, DeleteView):
    """
    Контроллер удаления пользователя
    """
    model = User
    success_url = reverse_lazy('users:user_list')

    def test_func(self):
        return self.user.is_superuser


@login_required()
@permission_required('users.set_active')
def block_user(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(User, pk=pk)
        obj.is_active = not obj.is_active
        obj.save()
        return redirect('users:user_list')
