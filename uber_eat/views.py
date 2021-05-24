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
from django.contrib import auth
from django.shortcuts import redirect
import random
from django.http import HttpResponse


def test(request):
    login_form = forms.LoginForm()
    return render(request, 'sign-in/signin.html', locals())


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
                    messages.add_message(request, messages.SUCCESS, 'success')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, 'warning')
            else:
                messages.add_message(request, messages.WARNING, 'fail')
        else:
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位內容')
    else:
        login_form = forms.LoginForm()
    return render(request, 'testLogin.html', locals())


def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.user.username
        useraddress = request.user.address
    messages.get_messages(request)
    return render(request, 'index.html', locals())


def logout(request):
    if 'username' in request.session:
        auth.logout(request)
        Session.objects.all().delete()
        messages.add_message(request, messages.INFO, "成功登出了")
        return redirect('/login/')
    return redirect('/')


def home(request):
    return render(request, 'carousel/index.html')


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


# ----------------------------------------------------------------
def test(request):
    return render(request, "index.html")


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
