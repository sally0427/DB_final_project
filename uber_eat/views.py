from django.shortcuts import render
from uber_eat.models import Store, Product, Oder, Consumer, Deliver
from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request, "index.html")

def add_store(self):
    # store_id = request.args.get("store_id")
    addStore = Store.objects.create(id = '5', address = 'aaa', name = '蔡家麵館', phone = '0800000123')
    addStore = Store(id = '5', address = 'aaa', name = '蔡家麵館', phone = '0800000123').save()
    return HttpResponse('<p>Add store</p>')

def add_product(self):
    addProduct = Product.objects.create(id = '5', store_id = '5', name = '番茄湯麵', price = '70')
    addProduct = Product(id = '5', store_id = '5', name = '番茄湯麵', price = '70').save()
    return HttpResponse('<p>Add product</p>')

def add_consumer(self):
    addConsumer = Consumer.objects.create(id = '1', address = 'aaa', name = '陳冠霖', phone = '0800000124')
    addConsumer = Consumer(id = '5', address = 'aaa', name = '陳冠霖', phone = '0800000124').save()
    return HttpResponse('<p>Add consumer</p>')

def add_deliver(self):
    addDeliver = Deliver.objects.create(id = '1', name = '司機', phone = '0800000125')
    addDeliver = Deliver(id = '1', name = '司機', phone = '0800000125').save()
    return HttpResponse('<p>Add deliver</p>')

def add_oder(self):
    addOder = Oder.objects.create(id = 1, consumer_id = 1, product_id = 5)
    addOder = Oder(id = 1, consumer_id = 1, product_id = 5).save()
    return HttpResponse('<p>Add oder</p>')