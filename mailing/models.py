from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    email = models.EmailField(max_length=100, verbose_name='email')
    comments = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=100, verbose_name='тема')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return {self.subject}

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):

    PERIODICITY_CHOICES = {
        'DAILY': 'ежедневно',
        'WEEKLY': 'еженедельно',
        'MONTHLY': 'ежемесячно',
    }

    STATUS_CHOICES = {
        'CREATED': 'создана',
        'IN_PROGRESS': 'в процессе',
        'COMPLETED': 'завершена',
    }

    start_mailing = models.DateTimeField(verbose_name='начало рассылки')
    end_mailing = models.DateTimeField(verbose_name='конец рассылки', **NULLABLE)
    periodicity = models.CharField(max_length=30, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='CREATED', verbose_name='статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    clients = models.ManyToManyField(Client, verbose_name='клиенты', **NULLABLE)

    def __str__(self):
        return f'С {self.start_mailing} {self.periodicity} ({self.status}).'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Attempt(models.Model):

    ATTEMPT_CHOICES = {
        'SUCCESS': 'успешно',
        'FAIL': 'неуспешно',
    }

    last_attempt = models.DateTimeField(verbose_name='последняя попытка', auto_now_add=True)
    status = models.CharField(max_length=50, choices=ATTEMPT_CHOICES, verbose_name='статус попытки')
    response = models.TextField(verbose_name='ответ сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f'{self.last_attempt} ({self.status})'

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
