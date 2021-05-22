from django.db import models

# Create your models here.
class Store(models.Model):
    Sid = models.IntegerField(primary_key=True)
    Sname = models.CharField(max_length=20, null=True)
    Saddress = models.CharField(max_length=20, null=True)
    Sphone = models.CharField(max_length=20, null=True)
    Stransit_price = models.DecimalField(max_digits=10, decimal_places=2, default='30')
    def __str__(self):
        return self.name #表示顯示cName欄位

class Product(models.Model):
    Pid = models.IntegerField(primary_key=True)
    Sid = models.ForeignKey(Store, on_delete=models.CASCADE, primary_key=False)
    Pname = models.CharField(max_length=20, null=True)
    Ptime = models.DateField(null=True)
    Pprice =  models.IntegerField(null=True)

class Deliver(models.Model):
    Did = models.IntegerField( primary_key=True)
    Dname = models.CharField(max_length=20, null=True)
    Dphone = models.CharField(max_length=20, null=True)

class Consumer(models.Model):
    Cid = models.IntegerField(primary_key=True)
    Cname = models.CharField(max_length=20, null=True)
    Cphone = models.CharField(max_length=20, null=True)
    Caddress = models.CharField(max_length=20, null=True)

class Order(models.Model):

    ORDER_STATUS_CHOICES = (
        (1, '正在建立訂單'),
        (2, '店家出貨'),
        (3, '外送員領貨'),
        (4, '外送員抵達'),
        (5, '消費者領取貨(結束訂單)')
    )

    Oid = models.IntegerField(primary_key=True)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, primary_key=False)
    Cid = models.ForeignKey(Consumer, on_delete=models.CASCADE, primary_key=False, null=False)
    Sid = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    Did = models.ForeignKey(Deliver, on_delete=models.CASCADE, primary_key=False, null=True)
    Ocount = models.IntegerField(default=0, verbose_name='商品數量')
    Oprice = models.IntegerField(default=0, verbose_name='商品總價')
    Ostatus = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='訂單狀態')
    Ocreated = models.DateTimeField(auto_now_add=True)

class OrderGoods(models.Model):
    OGid = models.IntegerField(primary_key=True)
    Oid = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    Pid = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=False)
    OGcount = models.IntegerField(default=1, verbose_name='商品數量')