from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    frase = models.CharField(max_length = 160)
    ubicacion = models.CharField(max_length = 50)
    avatar = models.CharField(max_length = 256)
    gender = models.CharField(max_length = 20, null=True)