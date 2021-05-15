"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from uber_eat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name ='test'),
    path('add_store/', views.add_store, name ='add_store'),
    path('add_store_post/', views.add_store_post, name ='add_store_post'),
    path('add_product/', views.add_product, name ='add_product'),
    path('add_product_post/', views.add_product_post, name ='add_product_post'),
    path('add_consumer/', views.add_consumer, name ='add_consumer'),
    path('add_consumer_post/', views.add_consumer_post, name ='add_consumer_post'),
    path('add_deliver/', views.add_deliver, name ='add_deliver'),
    path('add_deliver_post/', views.add_deliver_post, name ='add_deliver_post'),
    path('add_order_post/', views.add_order_post, name ='add_order_post'),
    path('add_ordergoods_post/', views.add_ordergoods_post, name ='add_ordergoods_post'),
    path('del_store/', views.del_store, name ='del_store'),
    path('del_store_post/', views.del_store_post, name ='del_store_post'),   
    path('del_product/', views.del_product, name ='del_product'),
    path('del_product_post/', views.del_product_post, name ='del_product_post'),
    path('del_consumer/', views.del_consumer, name ='del_consumer'),
    path('del_consumer_post/', views.del_consumer_post, name ='del_consumer_post'),  
]
