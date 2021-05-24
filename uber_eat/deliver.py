from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random
<<<<<<< HEAD
# Create your views here.
def test(request):
    return render(request, "index.html")

def add_deliver(request):
    return render(request, "add_deliver.html")

def add_deliver_post(request):
    random_num = random.randint(0,10000000)
    addDeliver = Deliver(Did = random_num, Dname = request.POST['Dname'], Dphone = request.POST['Dphone']).save()
    return HttpResponse('<p>Add deliver</p>')

def del_deliver(request):
    return render(request, "del_deliver.html")

def del_deliver_post(request):
    delDeliver = Deliver.objects.filter(Dname = request.POST['Dname']).delete()
    return HttpResponse('<p>Del deliver</p>')

def deliver_show_order(request):
    orders = Order.objects.filter(Ostatus=2)
    # S = Store.objects.get(Sid = orders.S_id)
    # Sname = S.Sname
    # Saddress = S.Saddress
    # Stransit_price = S.Stransit_price
    # C = Consumer.objects.get(Cid = orders.C_id)
    # Cphone = C.Cphone
    # Caddress = C.Caddress
    # context = {'Oid': orders.Oid,'Ocreated': orders.Ocreated,'Sname': Sname,'Saddress': Saddress,'Stransit_price': Stransit_price, 'Cphone': Cphone,'Caddress': Caddress}
    
    # for order in orders:
    #     S = Store.objects.get(Sid = order.S_id)
    #     Sname = S.Sname
    #     Saddress = S.Saddress
    #     Stransit_price = S.Stransit_price
    #     C = Consumer.objects.get(Cid = order.C_id)
    #     Cphone = C.Cphone
    #     Caddress = C.Caddress
    #     context = {'Oid': order.Oid,'Ocreated': order.Ocreated,'Sname': Sname,'Saddress': Saddress,'Stransit_price': Stransit_price, 'Cphone': Cphone,'Caddress': Caddress}
    # return orders
    return render(request, 'deliver_show_order.html', {'data': orders})
=======

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

def deliver_show_order(request):
    orders = Order.objects.filter(Ostatus=2).order_by('Oid')
    orderlist=list(orders)
    context = []
    for order in orderlist:
        S = Store.objects.get(Sid = order.S_id)
        Sname = S.Sname
        Saddress = S.Saddress
        Stransit_price = S.Stransit_price
        
        C = Consumer.objects.get(Cid = order.C_id)
        Cphone = C.Cphone
        Caddress = C.Caddress
        dict = {'Oid': order.Oid,'Ocreated': order.Ocreated,'Sname': Sname,'Saddress': Saddress,'Stransit_price': Stransit_price, 'Cphone': Cphone,'Caddress': Caddress}
        context.append(dict)
    return render(request, 'sally_api/deliver_show_order.html', {'data': context})
    
>>>>>>> origin
