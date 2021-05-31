# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from uber_store.models import Store, Product
from uber_deliver.models import Deliver


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        (1, '正在建立訂單'),
        (2, '店家已接單'),
        (3, '店家出貨'),
        (4, '外送員領貨'),
        (5, '外送員抵達'),
        (6, '消費者領取貨(結束訂單)')
    )

    Oid = models.AutoField(primary_key=True, auto_created=True)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, primary_key=False)
    C = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    S = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    D = models.ForeignKey(Deliver, on_delete=models.CASCADE, primary_key=False, null=True)
    Ocount = models.IntegerField(default=0, verbose_name='商品數量')
    Oprice = models.IntegerField(default=0, verbose_name='商品總價')
    Ostatus = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='訂單狀態')
    Ocreated = models.DateTimeField(auto_now_add=True)


class OrderGoods(models.Model):
    OGid = models.AutoField(primary_key=True, auto_created=True)
    O = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    P = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=False)
    OGcount = models.IntegerField(default=1, verbose_name='商品數量')
