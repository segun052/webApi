from django.db import models
from rest_framework.validators import UniqueValidator


# Create your models here.
class User(models.Model):

      email = models.EmailField(max_length=30) 
      address = models.CharField(max_length=1000)
      telephone = models.IntegerField()
      username = models.CharField(max_length=30)
      password = models.CharField(max_length=30)
