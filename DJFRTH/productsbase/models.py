from django.db import models
# Create your models here.
class base(models.Model):
    title = models.TextField(default='Some title', null=False, max_length='50')
    description = models.TextField(default='Some description', null=False, max_length='255')
    featured = models.BooleanField(default='True')
    number = models.IntegerField(default= 0, null=False)