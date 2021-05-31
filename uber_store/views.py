from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.urls import reverse

from uber_eat.models import Order
from uber_store import forms, models
from django.contrib.auth.models import User
from uber_eat.views import show_product
from django.contrib.auth.decorators import login_required


@login_required(login_url='/uber_eat/login/')
def add_product(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            Storeinfo = models.Store.objects.get(user=user)
            if request.method == 'POST':
                form = forms.addProductForm(request.POST)
                if form.is_valid():
                    Pname = request.POST['Pname'].strip()
                    Pprice = request.POST['Pprice']
                    models.Product.objects.create(S=Storeinfo, Pname=Pname, Pprice=Pprice)
                    return redirect('/uber_store')
                else:
                    messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
            else:
                form = forms.addProductForm()
        except:
            messages.add_message(request, messages.INFO, '頁面錯誤')
            return redirect('/')
    return render(request, 'registration/add_product.html', locals())


def show_product_img(ProductList):
    from django.db.models import Q
    q1 = Q()
    q1.connector = 'OR'
    for product in ProductList:
        q1.children.append(('P_id', product.Pid))
    PhotoList = models.Photo.objects.filter(q1).order_by('P_id')
    return PhotoList


@login_required(login_url='/uber_eat/login/')
def store_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            Storeinfo = models.Store.objects.get(user=user)
            if Storeinfo is not None:
                Sname = Storeinfo.Sname
                ProductList = show_product(Storeinfo.Sid)
                PhotoList = show_product_img(ProductList)
            if request.method == 'GET':
                models.Product.objects.filter(Pid=request.GET['Pid']).delete()
        except:
            pass
    return render(request, 'store/Edit_product.html', locals())


def home(request):
    form = forms.SignUpForm
    return render(request, 'registration/store_registration.html', locals())


@login_required(login_url='/uber_eat/login/')
def add_store_post(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            Storeinfo = models.Store.objects.get(user=user)
            if Storeinfo is not None:
                messages.add_message(request, messages.INFO, '您已經有商店了')
                return redirect('/')
        except:
            if request.method == 'POST':
                form = forms.SignUpForm(request.POST)
                if form.is_valid():
                    Sname = request.POST['Sname'].strip()
                    Sadderss = request.POST['Saddress']
                    Sphone = request.POST['Sphone']
                    models.Store.objects.create(user=user, Sname=Sname, Saddress=Sadderss, Sphone=Sphone)
                    return redirect('/')
                else:
                    messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
            else:
                form = forms.SignUpForm()
    return render(request, 'registration/store_registration.html', locals())
    # Store.objects.create(Sname='test', Saddress='At Earth', Sphone='123456789')


@login_required(login_url='/uber_eat/login/')
def upload_product_img(request):
    form = forms.UploadModelForm()
    productinfo = models.Product.objects.get(Pid=request.GET['Pid'])
    if request.method == "POST":
        form = forms.UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            productinfo.image = request.FILES['image']
            productinfo.save()
            return redirect('/uber_store')
    context = {
        'form': form
    }
    return render(request, 'sally_api/image.html', context)


@login_required(login_url='/uber_eat/login/')
def upload_store_img(request):
    form = forms.UploadModelForm()
    Storeinfo = models.Store.objects.get(Sid=request.GET['Sid'])
    if request.method == "POST":
        form = forms.UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            Storeinfo.image = request.FILES['image']
            Storeinfo.save()
            return redirect('/uber_store')
    context = {
        'form': form
    }
    return render(request, 'sally_api/image.html', context)


@login_required(login_url='/uber_eat/login/')
def store_show_order(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
            Storeinfo = models.Store.objects.get(user=userinfo)
            orders = Order.objects.filter(S=Storeinfo, Ostatus__lt=6).all().order_by('Ocreated')
            ordershistory = Order.objects.filter(S=Storeinfo, Ostatus=6).all().order_by('Ocreated')
        except:
            pass
        return render(request, 'orders/store_show_order.html', locals())


def store_get_order(request):
    try:
        orderinfo = Order.objects.get(Oid=request.GET['Oid'])
        orderinfo.Ostatus += 1
        orderinfo.save()
        return HttpResponseRedirect(reverse('store_show_order'))
    except:
        pass


def imgPer(file):
    from PIL import Image
    strin = 'D:/lessions/DB_final_project/media/'
    strin += str(file)
    print(strin)
    img = Image.open(strin)
    (w, h) = img.size
    print('w=%d, h=%d', w, h)
    new_img = img.resize((225, 225))
    new_img.save(strin)
