from django.contrib import messages
from django.shortcuts import render, redirect
from uber_deliver import forms
from django.contrib.auth.models import User
from uber_deliver import models
from django.contrib.auth.decorators import login_required
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
