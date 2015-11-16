from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re

# Create your models here.
class Profile(models.Model):
    def __unicode__(self):
        return str(self.user)
    user = models.ForeignKey(User)
    frase = models.CharField(max_length = 160)
    ubicacion = models.CharField(max_length = 50)
    avatar = models.CharField(max_length = 256)