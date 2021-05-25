from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Deliver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Did = models.AutoField(primary_key=True, auto_created=True)
    Dname = models.CharField(max_length=20, null=True)
    Dphone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Dname
