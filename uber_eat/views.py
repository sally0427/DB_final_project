from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request, "index.html")

def add_store(request):
    return render(request, "add_store.html")

def add_store_post(request):
    addStore = Store(id = request.POST['id'], address = request.POST['address'], name = request.POST['name'], phone = request.POST['phone'], transit_price = request.POST['transit_price']).save()
    return HttpResponse('<p>Add store</p>')

def add_product(request):
    return render(request, "add_product.html")

def add_product_post(request):
    addProduct = Product(id = request.POST['id'], store_id = request.POST['store_id'], name = request.POST['name'], price = request.POST['price']).save()
    return HttpResponse('<p>Add product</p>')

def add_consumer(request):
    return render(request, "add_consumer.html")

def add_consumer_post(request):
    addConsumer = Consumer(id = request.POST['id'], address = request.POST['address'], name = request.POST['name'], phone = request.POST['phone']).save()
    return HttpResponse('<p>Add consumer</p>')

def add_deliver(request):
    return render(request, "add_deliver.html")

def add_deliver_post(request):
    addDeliver = Deliver(id = request.POST['id'], name = request.POST['name'], phone = request.POST['phone']).save()
    return HttpResponse('<p>Add deliver</p>')

def add_order_post(self):
    addOrder = Order.objects.create(id = 1, consumer_id = 1, store_id = 1)
    addOrder = Order(id = 1, consumer_id = 1, store_id = 1).save()
    return HttpResponse('<p>Add Order</p>')

def add_ordergoods_post(self):
    # id = 1, order_id = 1, product_id = 1
    addOrdergoods = OrderGoods.objects.create(id = 2, order_id = 1, product_id = 2, count = 2)
    addOrdergoods = OrderGoods(id = 2, order_id = 1, product_id = 2, count = 2).save()
    return HttpResponse('<p>Add OrderGoods</p>')

def del_store(request):
    return render(request, "del_store.html")

def del_store_post(request):
    delProduct = Store.objects.filter(id = request.POST['id']).delete()
    return HttpResponse('<p>Del store</p>')

def del_product(request):
    return render(request, "del_product.html")

def del_product_post(request):
    delProduct = Product.objects.filter(id = request.POST['id']).delete()
    return HttpResponse('<p>Del product</p>')

def del_consumer(request):
    return render(request, "del_consumer.html")

def del_consumer_post(request):
    delConsumer = Consumer.objects.filter(id = request.POST['id']).delete()
    return HttpResponse('<p>Del consumer</p>')

def del_deliver(request):
    return render(request, "del_deliver.html")

def del_deliver_post(request):
    delDeliver = Deliver.objects.filter(id = request.POST['id']).delete()
    return HttpResponse('<p>Del deliver</p>')

def show_store(request):
    showStore = Store.objects.filter().all()
    return HttpResponse('<p>Add store</p>')