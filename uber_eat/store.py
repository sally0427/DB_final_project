from django.shortcuts import render
from uber_eat.models import OrderGoods, Product, Order, Deliver
from uber_store.models import Store
from django.http import HttpResponse
import random
import os
def del_store(request):
    return render(request, "sally_api/del_store.html")


def del_store_post(request):
    Store.objects.filter(Sname=request.POST['Sname']).delete()


def show_store(request):
    StoreList = Store.objects.filter().all().order_by('Sid')
    return StoreList
