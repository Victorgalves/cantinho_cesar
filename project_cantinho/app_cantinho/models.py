from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()  
 

class Vendinha(models.Model):
  name = models.CharField(max_length=200)
  products = models.ManyToManyField(Product)

class User(models.Model):
  name = models.CharField(max_length=200)
  products_cart = models.ManyToManyField(Product)

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  products = models.ManyToManyField(Product)
  total = models.DecimalField(max_digits=10, decimal_places=2)

class VendinhaController():
  def get_vendinha_by_name(name):
    return Vendinha.objects.get(name=name)
