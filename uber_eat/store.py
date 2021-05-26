from django.shortcuts import render
from uber_eat.models import OrderGoods, Product, Order, Deliver
from uber_store.models import Store
from django.http import HttpResponse
import random
import os

# def add_store(request):
#     return render(request, "sally_api/add_store.html")
#
#
# def add_store_post(request):
#     random_num = random.randint(0,10000000)
#     addStore = Store(Sid = random_num, Saddress = request.POST['Saddress'], Sname = request.POST['Sname'], Sphone = request.POST['Sphone'], Stransit_price = request.POST['Stransit_price']).save()
#     path = "static\\" + str(random_num) + "\\"
#     if not os.path.isdir(path):
#         os.makedirs(path)
#     return HttpResponse('<p>Add store</p>')



def del_store(request):
    return render(request, "sally_api/del_store.html")


def del_store_post(request):
    Store.objects.filter(Sname=request.POST['Sname']).delete()


def show_store(request):
    StoreList = Store.objects.filter().all().order_by('Sid')
    return StoreList
