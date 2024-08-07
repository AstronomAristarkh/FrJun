from django.core.management.base import BaseCommand
from ordersapp.models import Client


class Command(BaseCommand):
    help = "Get all users."
    
    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')