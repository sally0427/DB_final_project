from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from uber_eat.models import OrderGoods, Order
from uber_store.models import Store, Product
from uber_deliver.models import Deliver
from django.contrib.auth.models import User
from django.http import HttpResponse
import random

# def add_order(request):
#     return render(request, "sally_api/add_order.html")


# def add_order_post(request):
#     oid = random.randint(0,10000000)
#     Stransit_price = Store.objects.get(Sid = request.GET['S']).Stransit_price
#     addOrder = Order(Oid = oid, C_id = request.GET['C'], S_id = request.GET['S']).save()
#     Plist = request.GET.getlist('P')
#     price = 0
#     num = 0
#     for item in Plist:
#         random_num = random.randint(0,10000000)
#         Pid = item.split(',')[0]
#         count = item.split(',')[1]
#         price = price + int(Product.objects.get(Pid = Pid).Pprice)*int(count)
#         num = num + int(count)
#         addOrdergoods = OrderGoods(OGid = random_num, O_id = oid, P_id = Pid, OGcount = count).save()
#     price = price + Stransit_price
#     addOrder = Order.objects.filter(Oid = oid).update(Oprice = price, Ocount = num)
#     return redirect('/user_show_order')

# def mod_Ostatus_post(request):
#     addOrder = Order.objects.filter(Oid = request.POST['O']).update(Ostatus = request.POST['Ostatus'])
#     return HttpResponse('<p>mod_Ostatus_post</p>')

# def mod_Odeliver_post(request):
#     addOrder = Order.objects.filter(Oid = request.POST['O']).update(D_id = request.POST['Odeliver'])
#     return HttpResponse('<p>mod_Odeliver_post</p>')