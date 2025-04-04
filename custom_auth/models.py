from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15,unique=True)
    address = models.TextField(max_length=20,blank=True,null=True)
    birth_date = models.DateField(max_length=20,blank=True,null=True)
    is_verified = models.BooleanField(default=False)