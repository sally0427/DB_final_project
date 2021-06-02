import requests
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from uber_eat import forms
from uber_eat.forms import SignUpForm
from uber_deliver.models import Deliver
from uber_eat.models import *
from uber_store.models import Store, Product
from django.contrib import auth
from django.shortcuts import redirect
import random
from django.http import HttpResponse


def show_store(request):
    StoreList = Store.objects.filter().all().order_by('Sid')
    return StoreList


def search_store(request):
    StoreList = (Store.objects.filter(Sname__icontains=request.GET['Sname']) | Store.objects.filter(
        Stype__icontains=request.GET['Sname'])).all().order_by('Sid')
    return StoreList


@login_required(login_url='/uber_eat/login/')
def user_show_order(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
            orders = Order.objects.filter(C=userinfo, Ostatus__lt=6).all().order_by('Ocreated')
            ordershistory = Order.objects.filter(C=userinfo, Ostatus=6).all().order_by('Ocreated')
        except:
            pass
        return render(request, 'orders/consumer_show_order.html', locals())


@login_required(login_url='/uber_eat/login/')
def user_show_order_deteil(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
            order = Order.objects.get(Oid=request.GET['Oid'])
            orderdeteil = OrderGoods.objects.filter(O=order).all().order_by('P_id')
        except:
            pass
        return render(request, 'orders/order_base.html', locals())


@login_required(login_url='/uber_eat/login/')
def show_store_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
        except:
            pass
    if request.method == 'GET':
        Storeinfo = Store.objects.get(Sid=request.GET['Sid'])
        ProductList = Product.objects.filter(S_id=Storeinfo.Sid).order_by('Pid')
    return render(request, 'store/Show_product.html', locals())


def test(request):
    return render(request, 'store/Show_product.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print('success')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '使用者未啟用')
            else:
                messages.add_message(request, messages.WARNING, '使用者帳號或密碼錯誤')
        else:
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
    else:
        login_form = forms.LoginForm()
    return render(request, 'sign-in/signin.html', locals())


def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.user.username
        useraddress = request.user.address
    messages.get_messages(request)
    return render(request, 'index.html', locals())


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        # Session.objects.all().delete()
        return redirect('/uber_eat/login/')
    return redirect('/')


def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
            try:
                Storeinfo = Store.objects.get(user=userinfo)
                if Storeinfo is not None:
                    Sname = Storeinfo.Sname
            except:
                pass
            try:
                Deliverinfo = Deliver.objects.get(user=userinfo)
                if Deliverinfo is not None:
                    Dname = Deliverinfo.Dname
            except:
                pass
        except:
            pass
    try:
        data = search_store(request)
    except:
        data = show_store(request)

    return render(request, 'carousel/store_list.html', locals())


def insert(request):
    unit = Deliver.objects.create(id='1', name='test', phone='090909090')
    unit.save()
    Delivers = Deliver.objects.all().order_by('id')
    return render(request, 'index.html', locals())


class SingUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/user_registration.html'


@login_required(login_url='/uber_eat/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
        except:
            pass
    return render(request, 'userinfo.html', locals())


def add_order_post(request):
    oid = random.randint(0, 10000000)
    Stransit_price = Store.objects.get(Sid=request.GET['S']).Stransit_price
    addOrder = Order(Oid=oid, C_id=request.GET['C'], S_id=request.GET['S']).save()
    Plist = request.GET.getlist('P')
    price = 0
    num = 0
    for item in Plist:
        Pid = item.split(',')[0]
        count = item.split(',')[1]
        price = price + int(Product.objects.get(Pid=Pid).Pprice) * int(count)
        num = num + int(count)
        addOrdergoods = OrderGoods(O_id=oid, P_id=Pid, OGcount=count).save()
    price = price + Stransit_price
    addOrder = Order.objects.filter(Oid=oid).update(Oprice=price, Ocount=num)
    return redirect('/uber_eat/user_show_order')


def del_order(request):
    try:
        if request.method == 'GET':
            if Order.objects.get(Oid=request.GET['Oid'], Ostatus=1):
                OrderGoods.objects.filter(O_id=request.GET['Oid']).delete()
                Order.objects.filter(Oid=request.GET['Oid']).delete()
    except:
        pass
    return redirect('/uber_eat/user_show_order')


def store_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        Oid = request.GET['Oid']
        try:
            userinfo = User.objects.get(username=username)
            order = Order.objects.get(Ostatus=1, Oid=Oid)
            Storeinfo = Store.objects.get(Sid=order.S_id)
            if request.method == 'GET':
                ProductList = Product.objects.filter(S_id=Storeinfo.Sid).order_by('Pid')
                return render(request, 'orders/edit_order.html', locals())
            else:
                messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
        except:
            messages.add_message(request, messages.INFO, '頁面錯誤')
            return redirect('/')


def edit_order(request):
    OrderGoods.objects.filter(O_id=request.GET['Oid']).delete()
    Stransit_price = Store.objects.get(Sid=request.GET['S']).Stransit_price
    Plist = request.GET.getlist('P')
    price = 0
    num = 0
    for item in Plist:
        Pid = item.split(',')[0]
        count = item.split(',')[1]
        price = price + int(Product.objects.get(Pid=Pid).Pprice) * int(count)
        num = num + int(count)
        OrderGoods(O_id=request.GET['Oid'], P_id=Pid, OGcount=count).save()
    price = price + Stransit_price
    editOrder = Order.objects.filter(Oid=request.GET['Oid']).update(Oprice=price, Ocount=num)
    return redirect('/uber_eat/user_show_order')


def mod_Ostatus_post(request):
    addOrder = Order.objects.filter(Oid=request.POST['O']).update(Ostatus=request.POST['Ostatus'])
    return HttpResponse('<p>mod_Ostatus_post</p>')


def mod_Odeliver_post(request):
    addOrder = Order.objects.filter(Oid=request.POST['O']).update(D_id=request.POST['Odeliver'])
    return HttpResponse('<p>mod_Odeliver_post</p>')
