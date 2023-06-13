from django.db import models
from django.urls import reverse


class Product(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(max_length=500,null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'productId': self.pk})


class Category(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=500,null=True)


class CartLine(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    prod_name = models.CharField(null=True)
    quantity = models.IntegerField(null=True)
    price_for_one = models.IntegerField(null=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10,null=True)


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    cart_line = models.ForeignKey('CartLine', on_delete=models.SET_NULL, null=True)
    total_coast = models.DecimalField(decimal_places=2, max_digits=10,null=True)
