"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from products.views import MainCBV, ProductsCBV, ProductDetailCBV, products_create_vies, hello_view, \
    now_data, goodby
from djangoProject import settings
from users.views import auth_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainCBV.as_view()),
    path('products/', ProductsCBV.as_view()),
    path('products/create/', products_create_vies),
    path('products/<int:id>/', ProductDetailCBV.as_view(g)),
    path('hello/', hello_view),
    path('now_data/', now_data),
    path('goodby/', goodby),
    path('users/auth/', auth_view),
    path('users/register/', register_view),
    path('users/logout/', logout_view),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)