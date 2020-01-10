from django.db import models

# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=12)
    UserPassword = models.CharField(max_length=16)
