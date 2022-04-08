
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bookname=models.CharField(max_length=50)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=("username",)

    def __str__(self):
        return self.username
class book(models.Model):
      bookname=models.CharField(max_length=50)
      author=models.CharField(max_length=50)