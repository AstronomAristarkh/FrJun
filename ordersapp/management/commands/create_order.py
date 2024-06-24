from django.core.management.base import BaseCommand
from ordersapp.models import Order, Client, Product

class Command(BaseCommand):
    help = "Create order."
    def handle(self, *args, **kwargs):
        order = Order(client_id = Client.objects.filter(pk=1).first(), product_id = Product.objects.filter(pk=1).first(), amount = '100500', 
                      making_date = '1998-01-01')
        order.save()
        self.stdout.write(f'{order}')
