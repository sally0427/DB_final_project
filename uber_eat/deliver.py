from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random
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
    Orders = Order.objects.filter().get(Ostatus=2)
    Sname = Store.objects.get(Sid = Orders.S_id).Sname
    Cname = Consumer.objects.get(Cid = Orders.C_id).Cname
    # context = {'Oid': Oid,'Ocount': Ocount,'Oprice': Oprice,'Ocreated': Ocreated,'Sname': Sname, 'Cname': Cname}
    return render(request, 'deliver_show_order.html', {'data': Orders})