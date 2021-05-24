from django.shortcuts import render
from uber_eat.models import OrderGoods, Store, Product, Order, Consumer, Deliver
from django.http import HttpResponse
import random

def add_order(request):
<<<<<<< HEAD
    return render(request, "add_order.html")
=======
    return render(request, "sally_api/add_order.html")
>>>>>>> origin

def add_order_post(request):
    oid = random.randint(0,10000000)
    addOrder = Order(Oid = oid, C_id = request.POST['C'], S_id = request.POST['S']).save()
    Plist = request.POST.getlist('P')
<<<<<<< HEAD
=======
    price = 0
    num = 0
>>>>>>> origin
    for item in Plist:
        random_num = random.randint(0,10000000)
        Pid = item.split(',')[0]
        count = item.split(',')[1]
<<<<<<< HEAD
        addOrdergoods = OrderGoods(OGid = random_num, O_id = oid, P_id = Pid, OGcount = count).save()
=======
        price = price + Product.objects.get(Pid = Pid).Pprice
        num = num + int(count)
        addOrdergoods = OrderGoods(OGid = random_num, O_id = oid, P_id = Pid, OGcount = count).save()
    addOrder = Order.objects.filter(Oid = oid).update(Oprice = price, Ocount = num)
>>>>>>> origin
    return HttpResponse('<p>Add Order</p>')

def show_order(request):
    try:
<<<<<<< HEAD
        order = Order.objects.get(Oid = 2181925)
=======
        order = Order.objects.get(Oid = request.POST['Oid'])
>>>>>>> origin
    except:
        errormessage = " (讀取錯誤!)"
    Oid = order.Oid
    Ocount = order.Ocount
    Oprice = order.Oprice
    Ocreated = order.Ocreated
    Sname = Store.objects.get(Sid = order.S_id).Sname
    Cname = Consumer.objects.get(Cid = order.C_id).Cname
    context = {'Oid': Oid,'Ocount': Ocount,'Oprice': Oprice,'Ocreated': Ocreated,'Sname': Sname, 'Cname': Cname}
<<<<<<< HEAD
    return render(request, 'show_order.html', {'data': context})
=======
    return render(request, 'sally_api/show_order.html', {'data': context})
>>>>>>> origin

def mod_Ostatus_post(request):
    addOrder = Order.objects.filter(Oid = request.POST['O']).update(Ostatus = request.POST['Ostatus'])
    return HttpResponse('<p>mod_Ostatus_post</p>')

def mod_Odeliver_post(request):
    addOrder = Order.objects.filter(Oid = request.POST['O']).update(D_id = request.POST['Odeliver'])
    return HttpResponse('<p>mod_Odeliver_post</p>')
