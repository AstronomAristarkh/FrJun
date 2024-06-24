from django.core.management.base import BaseCommand
from ordersapp.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name = 'Chapelnik', description = 'ochen nuznaya and poleznaya vesht', price = 100500, quantity = 5, registration_date = '1998-01-01')
        product.save()

        self.stdout.write(f'{product}')
