from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random

def add_deliver(request):
    return render(request, "sally_api/add_deliver.html")


def add_deliver_post(request):
    random_num = random.randint(0, 10000000)
    addDeliver = Deliver(Did=random_num, Dname=request.POST['Dname'], Dphone=request.POST['Dphone']).save()
    return HttpResponse('<p>Add deliver</p>')


def del_deliver(request):
    return render(request, "sally_api/del_deliver.html")


def del_deliver_post(request):
    delDeliver = Deliver.objects.filter(Dname=request.POST['Dname']).delete()
    return HttpResponse('<p>Del deliver</p>')

