from django.db import models

# Create your models here.
class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, default='30')
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

class Order(models.Model):

    ORDER_STATUS_CHOICES = (
        (1, '正在建立訂單'),
        (2, '店家出貨'),
        (3, '外送員領貨'),
        (4, '外送員抵達'),
        (5, '消費者領取貨(結束訂單)')
    )

    id = models.IntegerField(primary_key=True)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, primary_key=False)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, primary_key=False, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE, primary_key=False, null=True)
    total_count = models.IntegerField(default=0, verbose_name='商品數量')
    total_price = models.IntegerField(default=0, verbose_name='商品總價')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='訂單狀態')
    created = models.DateTimeField(auto_now_add=True)

class OrderGoods(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=False)
    count = models.IntegerField(default=1, verbose_name='商品數量')