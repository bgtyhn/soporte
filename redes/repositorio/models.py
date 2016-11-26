from __future__ import unicode_literals

from django.db import models

class Token(models.Model):
	token = models.CharField(max_length = 5000)
	fileAddress = models.CharField(max_length = 5000)

# Create your models here.
