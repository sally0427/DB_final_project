from django.contrib import messages
from django.shortcuts import render, redirect
from uber_store import forms, models
from django.contrib.auth.models import User
from uber_eat.product import show_product
from django.contrib.auth.decorators import login_required


# Create your views here.
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
        except:
            messages.add_message(request, messages.INFO, '請先創立商店')
    return render(request, 'store/Show_product.html', locals())

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
