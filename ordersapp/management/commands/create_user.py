from django.core.management.base import BaseCommand
from ordersapp.models import Client

class Command(BaseCommand):
    help = "Create user."
    
    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', phone_number = '+7(111)111-11-11', 
                        adress = 'улица Ленина дом 1', registration_date = '1998-01-01')
        client.save()
        self.stdout.write(f'{client}')
