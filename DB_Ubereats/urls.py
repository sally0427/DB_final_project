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
from uber_eat import views, store, product, order, deliver
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

                  # ------------------------------------------------------

                  path('del_store/', store.del_store, name='del_store'),
                  path('del_store_post/', store.del_store_post, name='del_store_post'),
                  # path('show_store/', store.show_store, name='show_store'),

                  # path('add_product/', product.add_product, name='add_product'),
                  # path('add_product_post/', product.add_product_post, name='add_product_post'),
                  # path('del_product/', product.del_product, name='del_product'),
                  # path('del_product_post/', product.del_product_post, name='del_product_post'),
                  # path('show_product/', product.show_product, name='show_product'),

                  #   path('add_consumer/', consumer.add_consumer, name='add_consumer'),
                  #   path('add_consumer_post/', consumer.add_consumer_post, name='add_consumer_post'),
                  #   path('del_consumer/', consumer.del_consumer, name='del_consumer'),
                  #   path('del_consumer_post/', consumer.del_consumer_post, name='del_consumer_post'),

                  #   path('add_deliver/', deliver.add_deliver, name='add_deliver'),
                  #   path('add_deliver_post/', deliver.add_deliver_post, name='add_deliver_post'),
                  path('del_deliver/', deliver.del_deliver, name='del_deliver'),
                  path('del_deliver_post/', deliver.del_deliver_post, name='del_deliver_post'),

                  path('add_order/', order.add_order, name='add_order'),
                  path('add_order_post/', order.add_order_post, name='add_order_post'),
                  path('mod_Ostatus_post/', order.mod_Ostatus_post, name='mod_Ostatus_post'),
                  path('mod_Odeliver_post/', order.mod_Odeliver_post, name='mod_Odeliver_post'),
                  path('user_show_order/', order.user_show_order, name='user_show_order'),
                  path('store_show_order/', order.store_show_order, name='store_show_order'),
                  path('deliver_show_order/', order.deliver_show_order, name='deliver_show_order'),
                  path('upload_product_img/', product.upload_product_img, name='test')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
