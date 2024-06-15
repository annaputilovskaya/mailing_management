from django.core.management import BaseCommand

from mailing.cron import send_scheduled_mail


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_scheduled_mail()
