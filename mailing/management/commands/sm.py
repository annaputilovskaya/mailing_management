from django.core.management import BaseCommand

from mailing.cron import send_message


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_message(*args, **kwargs)
