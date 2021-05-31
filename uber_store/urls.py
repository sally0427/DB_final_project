"""DB_Ubereats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from uber_store import views

urlpatterns = [
    path('', views.store_page, name='store_page'),
    path('add_product', views.add_product, name='add_product'),
    path('joinStore/', views.add_store_post, name='home'),
    path('upload_product_img/', views.upload_product_img, name='upload_product_img'),
    path('upload_store_img/', views.upload_store_img, name='upload_store_img'),
    path('store_show_order/', views.store_show_order, name='store_show_order'),
    path('store_get_order/', views.store_get_order, name='store_get_order'),
]
