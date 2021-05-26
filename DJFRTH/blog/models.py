from django.db import models
# Create your models here.
class product(models.Model):
    title = models.TextField(default='New product')
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='worth that!')