from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(default='New product', max_length=100, null=False)
    description = models.CharField(default='Description', max_length=350)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=100)