from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random

def add_store(request):
<<<<<<< HEAD
    return render(request, "add_store.html")
=======
    return render(request, "sally_api/add_store.html")
>>>>>>> origin

def add_store_post(request):
    random_num = random.randint(0,10000000)
    addStore = Store(Sid = random_num, Saddress = request.POST['Saddress'], Sname = request.POST['Sname'], Sphone = request.POST['Sphone'], Stransit_price = request.POST['Stransit_price']).save()
    return HttpResponse('<p>Add store</p>')

def del_store(request):
<<<<<<< HEAD
    return render(request, "del_store.html")
=======
    return render(request, "sally_api/del_store.html")
>>>>>>> origin

def del_store_post(request):
    delProduct = Store.objects.filter(Sname = request.POST['Sname']).delete()
    return HttpResponse('<p>Del store</p>')

def show_store(request):
    StoreList = Store.objects.filter().all().order_by('Sid')
<<<<<<< HEAD
    return render(request, 'show_store.html', {'data': StoreList})
=======
    return render(request, 'sally_api/show_store.html', {'data': StoreList})
>>>>>>> origin
