from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random

def add_consumer(request):
    return render(request, "sally_api/add_consumer.html")

def add_consumer_post(request):
    random_num = random.randint(0,10000000)
    addConsumer = Consumer(Cid = random_num, Caddress = request.POST['Caddress'], Cname = request.POST['Cname'], Cphone = request.POST['Cphone']).save()
    return HttpResponse('<p>Add consumer</p>')

def del_consumer(request):
    return render(request, "sally_api/del_consumer.html")

def del_consumer_post(request):
    delConsumer = Consumer.objects.filter(Cname = request.POST['Cname']).delete()
    return HttpResponse('<p>Del consumer</p>')