from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    adress = models.TextField(max_length=100)
    registration_date = models.DateField()

    def __str__(self):
        return f'Имя: {self.name}, email: {self.email}, номер телефона: {self.phone_number}, адрес: {self.adress}, дата регистрации: {self.registration_date}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    registration_date = models.DateField()

    def __str__(self):
        return f'Имя: {self.name}, описание: {self.description}, цена: {self.price}, количество: {self.quantity}, дата регистрации: {self.registration_date}'


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default = 1)
    amount = models.IntegerField()
    making_date = models.DateField()
