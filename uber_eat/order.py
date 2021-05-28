from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from uber_eat.models import OrderGoods, Order
from uber_store.models import Store, Product
from uber_deliver.models import Deliver
from django.contrib.auth.models import User
from django.http import HttpResponse
import random

def add_order(request):
    return render(request, "sally_api/add_order.html")

def add_order_post(request):
    oid = random.randint(0,10000000)
    addOrder = Order(Oid = oid, C_id = request.GET['C'], S_id = request.GET['S']).save()
    Plist = request.GET.getlist('P')
    price = 0
    num = 0
    for item in Plist:
        random_num = random.randint(0,10000000)
        Pid = item.split(',')[0]
        count = item.split(',')[1]
        price = price + int(Product.objects.get(Pid = Pid).Pprice)*int(count)
        num = num + int(count)
        addOrdergoods = OrderGoods(OGid = random_num, O_id = oid, P_id = Pid, OGcount = count).save()
    addOrder = Order.objects.filter(Oid = oid).update(Oprice = price, Ocount = num)
    return redirect('/')


@login_required(login_url='/uber_eat/login/')
def user_show_order(request):
    # try:
    #     order = Order.objects.get(Oid = request.POST['Oid'])
    # except:
    #     errormessage = " (讀取錯誤!)"
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
            order = Order(C=userinfo)
            Oid = order.Oid
            Ocount = order.Ocount
            Oprice = order.Oprice
            Ocreated = order.Ocreated
            Cname = User.objects.get(id=order.C_id).username
            return render(request, 'sally_api/consumer_show_order.html', locals())
        except:
            errormessage = " (讀取錯誤!)"
            pass



def store_show_order(request):
    try:
        order = Order.objects.get(S_id = request.POST['Sid'])
    except:
        errormessage = " (讀取錯誤!)"
    Oid = order.Oid
    Ocount = order.Ocount
    Oprice = order.Oprice
    Ocreated = order.Ocreated
    Sname = Store.objects.get(Sid = order.S_id).Sname
    Cname = User.objects.get(Cid = order.C_id).Cname
    context = {'Oid': Oid,'Ocount': Ocount,'Oprice': Oprice,'Ocreated': Ocreated,'Sname': Sname, 'Cname': Cname}
    return render(request, 'sally_api/store_show_order.html', {'data': context})

def deliver_show_order(request):
    orders = Order.objects.filter(Ostatus=2).order_by('Oid')
    orderlist=list(orders)
    context = []
    for order in orderlist:
        S = Store.objects.get(Sid = order.S_id)
        Sname = S.Sname
        Saddress = S.Saddress
        Stransit_price = S.Stransit_price
        
        C = User.objects.get(Cid = order.C_id)
        Cphone = C.Cphone
        Caddress = C.Caddress
        dict = {'Oid': order.Oid,'Ocreated': order.Ocreated,'Sname': Sname,'Saddress': Saddress,'Stransit_price': Stransit_price, 'Cphone': Cphone,'Caddress': Caddress}
        context.append(dict)
    return render(request, 'sally_api/deliver_show_order.html', {'data': context})

def mod_Ostatus_post(request):
    addOrder = Order.objects.filter(Oid = request.POST['O']).update(Ostatus = request.POST['Ostatus'])
    return HttpResponse('<p>mod_Ostatus_post</p>')

def mod_Odeliver_post(request):
    addOrder = Order.objects.filter(Oid = request.POST['O']).update(D_id = request.POST['Odeliver'])
    return HttpResponse('<p>mod_Odeliver_post</p>')