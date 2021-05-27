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
    Stransit_price = models.DecimalField(max_digits=10, decimal_places=2, default='30')

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

class Photo(models.Model):
    # def user_directory_path(instance, filename):
    #     # file will be uploaded to MEDIA_ROOT/<Sid>/<Pid>
    #     return '{0}/{1}'.format(instance, filename)
    # user_directory_path
    P = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)