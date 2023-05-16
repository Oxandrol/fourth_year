from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from products.models import Products

from datetime import date

current_date = date.today()
print(current_date)




# Create your views here.

def main_page_view(request):
    if request.method == "GET":
        return render(request,'layouts/index.html')


def product_view(request):
    if request.method == "GET":

        products = Products.objects.all()

        data = {
            'products': products

        }

        return render(request, 'products/products.html', context=data)




