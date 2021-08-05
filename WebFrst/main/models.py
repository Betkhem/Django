from django.db import models

# Create your models here.


class CodeProblem(models.Model):
	title = models.TextField(max_length=100, null=False, blank=False, default='Name of this problem')
	description = models.CharField(max_length=1000, null=True, blank=True)
	