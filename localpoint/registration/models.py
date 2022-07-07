from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=35)
    email = models.EmailField
    user_photo = models.ImageField
    password = models.CharField(max_length=255)
    is_registered = models.BooleanField(default=True)
