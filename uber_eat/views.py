from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random
# Create your views here.
def test(request):
    return render(request, "index.html")

def add_store(request):
    return render(request, "add_store.html")

def add_store_post(request):
    random_num = random.randint(0,10000000)
    addStore = Store(Sid = random_num, Saddress = request.POST['Saddress'], Sname = request.POST['Sname'], Sphone = request.POST['Sphone'], Stransit_price = request.POST['Stransit_price']).save()
    return HttpResponse('<p>Add store</p>')

def add_product(request):
    return render(request, "add_product.html")

def add_product_post(request):
    random_num = random.randint(0,10000000)
    addProduct = Product(Pid = random_num, Sid = request.POST['Sid'], name = request.POST['Pname'], price = request.POST['Pprice']).save()
    return HttpResponse('<p>Add product</p>')

def add_consumer(request):
    return render(request, "add_consumer.html")

def add_consumer_post(request):
    random_num = random.randint(0,10000000)
    addConsumer = Consumer(Cid = random_num, Caddress = request.POST['Caddress'], Cname = request.POST['Cname'], Cphone = request.POST['Cphone']).save()
    return HttpResponse('<p>Add consumer</p>')

def add_deliver(request):
    return render(request, "add_deliver.html")

def add_deliver_post(request):
    random_num = random.randint(0,10000000)
    addDeliver = Deliver(Did = random_num, Dname = request.POST['Dname'], Dphone = request.POST['Dphone']).save()
    return HttpResponse('<p>Add deliver</p>')

def add_order_post(self):
    random_num = random.randint(0,10000000)
    addOrder = Order(id = random_num, consumer_id = 1, store_id = 1).save()
    return HttpResponse('<p>Add Order</p>')

def add_ordergoods_post(self):
    random_num = random.randint(0,10000000)
    addOrdergoods = OrderGoods(OGid = random_num, Oid = 1, Pid = 2, OGcount = 2).save()
    return HttpResponse('<p>Add OrderGoods</p>')

def del_store(request):
    return render(request, "del_store.html")

def del_store_post(request):
    delProduct = Store.objects.filter(Sname = request.POST['Sname']).delete()
    return HttpResponse('<p>Del store</p>')


def del_product(request):
    return render(request, "del_product.html")

def del_product_post(request):
    delProduct = Product.objects.filter(Pname = request.POST['Pname']).delete()
    return HttpResponse('<p>Del product</p>')

def del_consumer(request):
    return render(request, "del_consumer.html")

def del_consumer_post(request):
    delConsumer = Consumer.objects.filter(Cname = request.POST['Cname']).delete()
    return HttpResponse('<p>Del consumer</p>')

def del_deliver(request):
    return render(request, "del_deliver.html")

def del_deliver_post(request):
    delDeliver = Deliver.objects.filter(Dname = request.POST['Dname']).delete()
    return HttpResponse('<p>Del deliver</p>')

def show_store(request):
    showStore = Store.objects.filter().all()
    return render(request, 'show_store.html', {'data': showStore})