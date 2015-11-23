from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    frase = models.CharField(max_length = 160, null=True)
    ubicacion = models.CharField(max_length = 50, null=True)
    avatar = models.CharField(max_length = 256, null=True)
    gender = models.CharField(max_length = 20, null=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)