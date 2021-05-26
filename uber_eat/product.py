
from django.shortcuts import render, redirect
from uber_eat.models import OrderGoods, Order, Photo
from uber_store.models import Store, Product
from uber_deliver.models import Deliver

from django.http import HttpResponse
import random
import os
from .forms import UploadModelForm

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

def upload_product_img(request):
    photos = Photo.objects.all()
    form = UploadModelForm()
    if request.method == "POST":
        Sid = Store.objects.get(Sid = request.POST['Sid']).Sid
        Pid = Product.objects.get(Pid = request.POST['Pid']).Pid
        form = UploadModelForm(request.POST, request.FILES, Sid, Pid)
        if form.is_valid():
            form.save()
            return redirect('/uber_eat')
    context = {
        'uber_eat': photos,
        'form': form
    }
    return render(request, 'sally_api/image.html', context)

def show_product(Sid):
    ProductList = Product.objects.filter(S_id=Sid).order_by('Pid')
    return ProductList
