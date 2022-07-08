from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=35)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    is_registered = models.BooleanField(default=True)
