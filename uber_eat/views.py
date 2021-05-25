from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from uber_eat import forms
from uber_eat.forms import SignUpForm
# Create your views here.
from uber_eat.models import *
from uber_store import models
from django.contrib import auth
from django.shortcuts import redirect
from uber_eat.store import show_store
import random
from django.http import HttpResponse


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
        Session.objects.all().delete()
        return redirect('/uber_eat/login/')
    return redirect('/')


def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
            try:
                Storeinfo = models.Store.objects.get(user=userinfo)
                if Storeinfo is not None:
                    Sname = Storeinfo.Sname
            except:
                pass
        except:
            pass
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


def joinStore(request):
    return render(request, 'store/storeRegistration.html')


@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            userinfo = User.objects.get(username=username)
        except:
            pass
    return render(request, 'userinfo.html', locals())
