from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=256, blank=False, null=False)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.EmailField(max_length=256)
    fullname = models.CharField(max_length=256)
