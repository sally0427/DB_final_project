from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from uber_deliver import forms
from django.contrib.auth.models import User
from uber_deliver import models
from django.contrib.auth.decorators import login_required
from uber_eat.models import Order, OrderGoods


# Create your views here.


@login_required(login_url='/uber_eat/login/')
def add_deliver_post(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            DeliverInfo = models.Deliver.objects.get(user=user)
            if DeliverInfo is not None:
                messages.add_message(request, messages.INFO, '您已經是外送員了')
                return redirect('/')
        except:
            if request.method == 'POST':
                form = forms.SignUpForm(request.POST)
                if form.is_valid():
                    Dname = request.POST['Dname'].strip()
                    Dphone = request.POST['Dphone']
                    models.Deliver.objects.create(user=user, Dname=Dname, Dphone=Dphone)
                    return redirect('/')
                else:
                    messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
            else:
                form = forms.SignUpForm()
    return render(request, 'registration/deliver_registration.html', locals())


@login_required(login_url='/uber_eat/login/')
def show_deliver_order(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
            DeliverInfo = models.Deliver.objects.get(user=userinfo)
            orders = (Order.objects.filter(D=None, Ostatus=3) | Order.objects.filter(D=None, Ostatus=2)).all().order_by('Ocreated')
            deliverorders = Order.objects.filter(D=DeliverInfo).all().order_by('Ocreated')
        except:
            pass
        return render(request, 'orders/deliver_show_order.html', locals())


def deliver_get_order(request):
    try:
        orderinfo = Order.objects.get(Oid=request.GET['Oid'])
        if orderinfo.Ostatus == 3:
            orderinfo.D = models.Deliver.objects.get(user=request.user)
        orderinfo.Ostatus += 1
        orderinfo.save()
        return HttpResponseRedirect(reverse('show_deliver_order'))
    except:
        pass
