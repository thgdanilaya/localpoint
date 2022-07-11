from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=35)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    is_registered = models.BooleanField(default=True)
    is_online = models.BooleanField(default=False)
    tokenn = models.CharField(max_length=255, default="", null=True)


# class UserProfile(models.Model):
#     username = models.CharField(max_length=35)
#     email = models.CharField(max_length=255)
#     account_type = models.CharField(max_length=40)
#
#     # profile_pic = models.ImageField(blank=True)
#
#     def __str__(self):
#         return str(self.username)
