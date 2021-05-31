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
from uber_eat.views import SingUpView
from uber_eat import views

urlpatterns = [
    path('signup/', SingUpView.as_view(), name='signup'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('store/', views.show_store_page, name='show_store_page'),
    path('user_show_order/', views.user_show_order, name='user_show_order'),
    path('add_order_post/', views.add_order_post, name='add_order_post'),
    path('mod_Ostatus_post/', views.mod_Ostatus_post, name='mod_Ostatus_post'),
    path('mod_Odeliver_post/', views.mod_Odeliver_post, name='mod_Odeliver_post'),
    path('user_show_order_deteil/', views.user_show_order_deteil, name='user_show_order_deteil')
]
