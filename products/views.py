import os

from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView

from djangoProject import settings
from products.forms import ProductCreateForm
from products.models import Products, Comment
from products import forms
from products.constants import PAGINATIONLIMIT

from datetime import date

current_date = date.today()
print(current_date)


# Create your views


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my first view ')


def now_data(request):
    if request.method == 'GET':
        return HttpResponse(current_date)


def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


class MainCBV(ListView):
    model = Products
    template_name = 'layouts/index.html'


class ProductsCBV(ListView):
    model = Products
    queryset = Products.objects.all()
    template_name = 'products/products.html'

    def get(self, request, *args, **kwargs):
        products = self.queryset
        search = request.GET.get('search')
        page = int(request.GET.get('page'))

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
            'page': range(1, max_page + 1)

        }

        return render(request, self.template_name, context=data)


class CommentsCreateForm:
    pass


class ProductDetailCBV(DetailView, CreateView):
    model = Products
    template_name = 'products/detail.html'
    form_class = CommentsCreateForm
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'product': self.get_object(),
            'Comments': Comment.objects.filter(product=self.get_object()),
            'form': kwargs.get('form', self.form_class)
        }

    def post(self, request, **kwargs):
        data = request.POST
        form = CommentsCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=self.get_object().id
            )
            return redirect(f'/products/{self.get_object().id}/')

        return render(request, self.template_name, context=self.get_context_data(form=form))


def products_create_vies(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'PRODUCT':
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


class FormValidator:

    def __init__(self, fields: dict = None, non_reqiured: list = None):
        self.fields = fields
        self.non_required = non_reqiured

    def is_valid(self):
        """
        this method need for check fields
        """
        pass

    def validated_data(self) -> dict:
        """
        return dict of validated data
        ATTENTION: call this method after call is_valid()
        """
        pass