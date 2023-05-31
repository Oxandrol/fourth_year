from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from products.models import Products, Comment
from products.forms import ProductCreateForm
from products.constants import PAGINATIONLIMIT

from datetime import date

current_date = date.today()



# Create your views here.

def main_page_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == "GET":
        products = Products.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = products.__len__() / PAGINATIONLIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATIONLIMIT * (page - 1):PAGINATIONLIMIT * page]

        if search:
            products = products.filter(title__contains=search) | products.filter(description__contains=search)

        data = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
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
