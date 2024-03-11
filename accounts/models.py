from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)
    photo = models.ImageField(upload_to='photo/profile/%Y/%m/%d/',default='null')
    about = models.CharField(max_length=225,default='null')