from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Sid = models.AutoField(primary_key=True, auto_created=True)
    Sname = models.CharField(max_length=20, null=True)
    Saddress = models.CharField(max_length=20, null=True)
    Sphone = models.CharField(max_length=20, null=True)
    Stransit_price = models.DecimalField(max_digits=10, decimal_places=2, default='30')

    def __str__(self):
        return self.Sname


class Product(models.Model):
    Pid = models.AutoField(primary_key=True, auto_created=True)
    S = models.ForeignKey(Store, on_delete=models.CASCADE)
    Pname = models.CharField(max_length=20, null=True)
    Ptime = models.DateField(null=True)
    Pprice = models.IntegerField(null=True)
