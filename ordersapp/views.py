from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Product, Order
from django.core.files.storage import FileSystemStorage
from .forms import PictForm


def index(request):
    return HttpResponse("Welcome to our shop!")


class Last(View):
    def get(self, request, clientid, days):
        orders = Order.objects.filter(client_id=clientid)
        pokupky = []
        for i in range (len(orders)):
            if orders[i].making_date >= date.today()-timedelta(days):    
                pokupky.append(Product.objects.filter(id = orders[i].product_id.pk).first().name)
        context = {'spisok':pokupky}
        return render(request, 'ordersapp/last.html', context)

def load_picture_form(request):
    if request.method == 'POST':
        form = PictForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            registration_date = form.cleaned_data['registration_date']
            image = form.cleaned_data['image']
            product = Product(name=name, description=description, price=price, quantity=quantity, 
                              registration_date=registration_date, image=image)
            product.save()
            message = 'Пользователь сохранён'
    else:
        form = PictForm()
        message = 'Заполните форму'
    return render(request, 'ordersapp/load_picture.html', {'form':form, 'message': message})

