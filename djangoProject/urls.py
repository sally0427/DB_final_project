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
    path('add_product/', views.add_product, name ='add_product'),
    path('add_oder/', views.add_oder, name ='add_oder'),
    path('add_consumer/', views.add_consumer, name ='add_consumer'),
    path('add_deliver/', views.add_deliver, name ='add_deliver'),
]
