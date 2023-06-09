from django.db import models
from django.urls import reverse


class Product(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'productId': self.pk})


class Category(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


class CartLine(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    prod_name = models.CharField()
    quantity = models.IntegerField()
    price_for_one = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10)


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    cart_line = models.ForeignKey('CartLine', on_delete=models.SET_NULL, null=True)
    total_coast = models.DecimalField(decimal_places=2, max_digits=10)
