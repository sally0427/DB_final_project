from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random

def add_product(request):
    return render(request, "add_product.html")

def add_product_post(request):
    random_num = random.randint(0,10000000)
    addProduct = Product(Pid = random_num, S_id = request.POST['S'], Pname = request.POST['Pname'], Pprice = request.POST['Pprice']).save()
    return HttpResponse('<p>Add product</p>')

def del_product(request):
    return render(request, "del_product.html")

def del_product_post(request):
    delProduct = Product.objects.filter(Pname = request.POST['Pname']).delete()
    return HttpResponse('<p>Del product</p>')