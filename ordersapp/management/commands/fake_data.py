from django.core.management.base import BaseCommand
from ordersapp.models import Client, Product, Order
import random


class Command(BaseCommand):
    help = "Generate fake authors and posts."
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        #for i in range(1, count + 1):
        #    client = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', phone_number = f'+7{random.randint(1000000000, 9999999999)}', 
        #                    adress = f'ул. Советская, д. {random.randint(1,150)}', 
        #                    registration_date = f'202{random.randint(0,4)}-{random.randint(10,12)}-{random.randint(10,30)}')
        #    client.save()
        #for j in range(1, count + 1):
        #    product = Product(name = f'Title{j}',
        #                      description = f'Description of title #{j} is bla bla bla many long text',
        #                      price = random.randint(1,150),
        #                      quantity = random.randint(1,150),
        #                      registration_date = f'202{random.randint(0,4)}-{random.randint(10,12)}-{random.randint(10,30)}')
        #    product.save()
        for k in range(1, count + 1):
            order = Order(client_id = Client.objects.filter(pk=random.randint(1,50)).first(), 
                          product_id = Product.objects.filter(pk=random.randint(1,50)).first(), amount = random.randint(1,1500), 
                          making_date = f'202{random.randint(0,4)}-{random.randint(10,12)}-{random.randint(10,30)}')
            order.save()
