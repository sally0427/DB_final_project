from django.db import models

# Create your models here.
class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name #表示顯示cName欄位

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, primary_key=False)
    name = models.CharField(max_length=20, null=True)
    time = models.DateField(null=True)
    price =  models.IntegerField(null=True)

class Deliver(models.Model):
    id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)

class Consumer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)
