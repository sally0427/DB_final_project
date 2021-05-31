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
from django.contrib import admin
from django.urls import path, include
from uber_eat import views, store, product, order
from uber_store.models import Photo
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('insert/', views.insert, name='insert'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('uber_eat/', include('uber_eat.urls')),
                  path('uber_store/', include('uber_store.urls')),
                  path('uber_deliver/', include('uber_deliver.urls')),
                  path('', views.home, name='home'),
                  path('userinfo/', views.userinfo),
                  path('test/', views.test),

                  path('add_order/', views.add_order, name='add_order'),
                  path('add_order_post/', views.add_order_post, name='add_order_post'),
                  path('mod_Ostatus_post/', views.mod_Ostatus_post, name='mod_Ostatus_post'),
                  path('mod_Odeliver_post/', views.mod_Odeliver_post, name='mod_Odeliver_post'),
                  

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
