from django.db import models
from product.models import Product
from django.contrib.auth.models import User
import datetime
from django import forms

# Create your models here.


class Ecart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table='ecart'






    











