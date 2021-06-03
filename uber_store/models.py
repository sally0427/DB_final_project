from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Sid = models.AutoField(primary_key=True, auto_created=True)
    Sname = models.CharField(max_length=20, null=True)
    Saddress = models.CharField(max_length=20, null=True)
    Sphone = models.CharField(max_length=20, null=True)
    Stype = models.TextField(null=True, default=None)
    Stransit_price = models.DecimalField(max_digits=10, decimal_places=0, default='30')
    image = models.ImageField(upload_to='product_image/', blank=False, null=True, default=None)
    def __str__(self):
        return self.Sname


class Product(models.Model):
    Pid = models.AutoField(primary_key=True, auto_created=True)
    S = models.ForeignKey(Store, on_delete=models.CASCADE)
    Pname = models.CharField(max_length=20, null=True)
    Ptime = models.DateField(null=True)
    Pprice = models.IntegerField(null=True)
    image = models.ImageField(upload_to='product_image/', blank=False, null=True, default=None)
    upload_date = models.DateField(default=timezone.now)


