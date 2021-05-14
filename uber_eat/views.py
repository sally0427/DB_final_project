from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request, "index.html")


def add_store_get(request):
    return render(request, "add_store.html")

def add_store(request):
    addStore = Store(id = request.POST['id'], address = request.POST['address'], name = request.POST['name'], phone = request.POST['phone'], transit_price = request.POST['transit_price']).save()
    return HttpResponse('<p>Add store</p>')

def add_product_get(request):
    return render(request, "add_product.html")

def add_product(request):
    addProduct = Product(id = request.POST['id'], store_id = request.POST['store_id'], name = request.POST['name'], price = request.POST['price']).save()
    return HttpResponse('<p>Add product</p>')

def add_consumer_get(request):
    return render(request, "add_consumer.html")

def add_consumer(request):
    addConsumer = Consumer(id = request.POST['id'], address = request.POST['address'], name = request.POST['name'], phone = request.POST['phone']).save()
    return HttpResponse('<p>Add consumer</p>')

def add_deliver_get(request):
    return render(request, "add_deliver.html")

def add_deliver(request):
    addDeliver = Deliver(id = request.POST['id'], name = request.POST['name'], phone = request.POST['phone']).save()
    return HttpResponse('<p>Add deliver</p>')

def add_order(self):
    addOrder = Order.objects.create(id = 1, consumer_id = 1, store_id = 1)
    addOrder = Order(id = 1, consumer_id = 1, store_id = 1).save()
    return HttpResponse('<p>Add Order</p>')

def add_ordergoods(self):
    # id = 1, order_id = 1, product_id = 1
    addOrdergoods = OrderGoods.objects.create(id = 2, order_id = 1, product_id = 2, count = 2)
    addOrdergoods = OrderGoods(id = 2, order_id = 1, product_id = 2, count = 2).save()
    return HttpResponse('<p>Add OrderGoods</p>')


