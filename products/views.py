from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from products.models import Products, Comment
from products.forms import ProductCreateForm

from datetime import date

current_date = date.today()
print(current_date)


# Create your views here.

def main_page_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def product_view(request):

    if request.method == "GET":
        products = Products.objects.all()

        data = {
            'products': products,
            'user': request.user
        }

        return render(request, 'products/products.html', context=data)


def product_deail_view(request, id_):
    if request.method == "GET":
        product = Products.objects.get(id=id_)

        context = {
            'product': product,
            'comments': product.comment_set.all()
        }

        return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == "GET":
        context = {
            'form': ProductCreateForm

        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')

            )

            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })
