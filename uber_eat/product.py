from django.shortcuts import render
from uber_eat.models import OrderGoods, Order, Consumer
from uber_store.models import Store, Product
from uber_deliver.models import Deliver
from django.http import HttpResponse
import random

def add_product(request):
    return render(request, "sally_api/add_product.html")

def add_product_post(request):
    random_num = random.randint(0,10000000)
    addProduct = Product(Pid = random_num, S_id = request.POST['S'], Pname = request.POST['Pname'], Pprice = request.POST['Pprice']).save()
    return HttpResponse('<p>Add product</p>')

def del_product(request):
    return render(request, "sally_api/del_product.html")

def del_product_post(request):
    delProduct = Product.objects.filter(Pname = request.POST['Pname']).delete()
    return HttpResponse('<p>Del product</p>')

def show_product(Sid):
    # ProductList = Product.objects.filter(S_id=request.POST['S']).order_by('Pid')
    # Sname = Store.objects.get(Sid = request.POST['S']).Sname
    ProductList = Product.objects.filter(S_id=Sid).order_by('Pid')
    Sname = Store.objects.get(Sid=Sid).Sname
    return ProductList
    # return render('sally_api/show_product.html', {'data': ProductList, 'Sname': Sname})