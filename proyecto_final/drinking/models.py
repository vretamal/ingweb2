# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re

RON = 'RN'
PISCO = 'PS'
VOKDA = 'VK'
GIN = 'GN'
CERVEZA = 'CR'
JUGO = 'JG'
TEQUILA = 'TQ'
BEBIDA = 'BB'
WISKEY = 'WK'
VINO = 'VN'
AGUA_ARDIENTE = 'AA'

TIPO_CHOICES = (
    (RON, 'Ron'),
    (PISCO, 'Pisco'),
    (VOKDA, 'Vokda'),
    (GIN, 'Gin'),
    (CERVEZA, 'Cerveza'),
    (JUGO, 'Jugo'),
    (TEQUILA, 'Tequila'),
    (BEBIDA, 'Bebida'),
    (WISKEY, 'Wiskey'),
    (VINO, 'Vino'),
    (AGUA_ARDIENTE, 'Agua Ardiente'),
)
# Create your models here.
####    INGREDIENTES
class Ingrediente(models.Model):

    tipo = models.CharField(max_length = 15, choices=TIPO_CHOICES, default=RON)
    marca =  models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 100)
    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
        ordering = ['tipo']


    def __unicode__(self):
        return "%s %s" % (self.get_tipo_display(), self.marca)



####    RUBRO
class Rubro(models.Model):
    BAR = 'BR'
    PUB = 'PB'
    DISCO = 'DS'
    RESTORANT = 'RS'

    RUBRO_COICES = (
        (BAR, 'Bar'),
        (PUB, 'Pub'),
        (DISCO, 'Disco'),
        (RESTORANT, 'Restorant'),
    )

    nombre = models.CharField(max_length = 2,
                              choices=RUBRO_COICES, default=BAR)
    class Meta:
        verbose_name = "Rubro"
        verbose_name_plural = "Rubros"

    def __unicode__(self):
        return self.nombre






####    LOCAL
class Local(models.Model):
    # user = models.OneToOneField(User, null=True)
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 200)
    ubicacion = models.CharField(max_length = 50, null=True)
    horario = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 100)
    rubros = models.ForeignKey(Rubro, null=True)
    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"

    def __unicode__(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion


####    CARTA
class Carta(models.Model):
    nombre = models.CharField(max_length = 30, default='carta')
    local = models.ForeignKey(Local)
    class Meta:
        verbose_name = "Carta"
        verbose_name_plural = "Cartas"

    def __unicode__(self):
        return "Carta de " + self.local.nombre


####    PRODUCTO
class Producto(models.Model):
    nombre = models.CharField(max_length = 30)
    ingredientes = models.ManyToManyField(Ingrediente)
    carta = models.ForeignKey(Carta, null=True)
    local = models.ForeignKey(Local, null=True)
    precio = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __unicode__(self):
        return self.nombre


# ####    CARTAPRODUCTO
# class CartaProducto(models.Model):
#     precio = models.IntegerField(default=2)
#     carta = models.ForeignKey(Carta)
#     producto = models.ForeignKey(Producto)

#     class Meta:
#         verbose_name = "CartaProducto"
#         verbose_name_plural = "CartaProductos"

#     def __unicode__(self):
#         return "Carta: %s, Producto: %s" % (self.carta, self.producto.nombre)



####    PROFILE
class Profile(models.Model):
    user = models.OneToOneField(User)
    frase = models.CharField(max_length = 160, null=True)
    ubicacion = models.CharField(max_length = 50, null=True)
    avatar = models.CharField(max_length = 256, null=True)
    gender = models.CharField(max_length = 20, null=True)
    locales = models.ManyToManyField(Local)

    def __unicode__(self):
        return "%s's profile" % self.user

    def is_admin(self):
        if self.user.role == roles.admin:
            return True
        else:
            return False

class Admin(models.Model):
    user = models.OneToOneField(User)
    local = models.OneToOneField(Local)

    def __unicode__(self):
        return "%s's Admin profile" % self.user

####    OTRO
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
