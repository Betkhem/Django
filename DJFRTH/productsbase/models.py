from django.db import models
# Create your models here.
class base(models.Model):
    title = models.CharField(default='Some title', null=False, max_length=100)
    description = models.TextField(default='New description', null=False, max_length='255')
    price = models.DecimalField(default= 0, null=False, max_digits=50, decimal_places=2)
    summary = models.TextField(default='This is summary', max_length='100')
    featured = models.BooleanField(default='True')