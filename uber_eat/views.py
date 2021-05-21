from django.shortcuts import render
from django.views.generic import CreateView
from uber_eat.forms import SignUpForm
# Create your views here.
from uber_eat.models import *


def home(request):
    return render(request, 'registration/registration.html')


def insert(request):
    unit = Deliver.objects.create(id='1', name='test', phone='090909090')
    unit.save()
    Delivers = Deliver.objects.all().order_by('id')
    return render(request, 'index.html', locals())

def SignupBack(request):
    units = User.objects.all().filter(typein=False, type='consumer')
    print(units)
    for unit in User.objects.all().filter(type='consumer', typein=False):
        print(unit)
        Cons = Consumer.objects.create(id=unit.id, name=unit.username, phone=unit.phone)
        Cons.save()
        Consumers = Consumer.objects.all().order_by('id')
    return render(request, 'index.html', locals())

class SingUpView(CreateView):
    form_class = SignUpForm
    # success_url = reverse_lazy('login')
    success_url = 'backCheck'
    template_name = 'registration/registration.html'
