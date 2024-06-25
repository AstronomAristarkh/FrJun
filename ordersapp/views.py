from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Product, Order



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
