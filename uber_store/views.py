from django.shortcuts import render
from uber_store import forms
from uber_eat.models import Store


# Create your views here.

def home(request):
    form = forms.SignUpForm
    return render(request, 'store/storeRegistration.html', locals())


def add_store_post(request):
    Store.objects.create(Sname='test', Saddress='At Earth', Sphone='123456789')
    return home()
