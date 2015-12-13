# -*- encoding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import *
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context import RequestContext
from django.views import generic
from drinking.models import *
import json


# class HomeView(generic.TemplateView):
#     template_name = "drinking/home.html"

def home(request):
    user = request.user
    if user.is_authenticated():
        profile = user.profile
    return render(request, 'drinking/home.html')


@staff_member_required
def localhome(request):
    user = request.user
    try:
        admin = user.admin
        local = admin.local
    except:
        return

    try:
        carta = Carta.objects.get(local = local)
    except:
        carta = None

    return render(request, 'drinking/mylocal.html',
                  { 'local':local, 'carta' : carta })


@staff_member_required
def crearCarta(request):
    local = request.user.admin.local
    carta = Carta.objects.get_or_create(local=local)
    return localhome(request)


# def anadirElementoCarta(request):
#     local = request.user.admin.local
#     carta = Carta.objects.get(local = local)
#     if request.method == 'POST':
#         q_producto = request.POST['producto']
#         producto = Producto.objects.get(id=q_producto)
#         precio = request.POST['precio']
#         CartaProducto.objects.create(producto = producto, precio = precio, carta = carta)

#     productos_de_carta = CartaProducto.objects.filter(carta = carta)

#     # return render(request, 'drinking/mylocal.html', { 'local': local, 'carta' : carta, 'productos' : productos})
#     return render(request,'drinking/mylocal.html',
#                        { 'local':local, 'carta':carta,
#                        'cartaProductos':productos_de_carta})


def test(request):
    return render(request, 'drinking/testadmin.html')




# PETICIONES AJAX

def anadirElementoCarta(request):
    if request.method == 'POST':
        local = request.user.admin.local
        carta = Carta.objects.get(local = local)
        producto_id = request.POST.get('producto')
        producto = Producto.objects.get(id=producto_id)
        response_data = {}
        precio = request.POST.get('precio')

        response_data['result'] = 'Create post successful!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def getCarta(request):
    local = request.user.admin.local
    carta = Carta.objects.get(local = local)
    productos = producto
    data = serializers.serialize('json', productos,
                                 fields=('id', 'precio'))


def anadirProducto(request):
    local = request.user.admin.local
    carta = Carta.objects.get(local = local)
    ingredientes = Ingrediente.objects.all()

    return render(request, 'drinking/admin/nuevoProducto.html',
                  {'local' : local, 'carta' : carta,
                  'ingredientes' : ingredientes, 'choices' : TIPO_CHOICES})

def anadirProducto_AJAX(request):
    local = request.user.admin.local
    carta = Carta.objects.get(local = local)
    id_ing = request.GET['id_ing']
    ingredientes = Ingrediente.objects.filter(tipo = id_ing)
    data = serializers.serialize('json', ingredientes, fields=('marca', 'pk'))

    return HttpResponse(data, content_type='application/json')

    # return render(request, 'drinking/admin/nuevoProducto.html',
    #               {'local' : local, 'carta' : carta,
    #               'ingredientes' : ingredientes, 'choices' : TIPO_CHOICES})

def crearProducto_AJAX(request):
    local = request.user.admin.local
    carta = Carta.objects.get(local = local)
    ingredientes = request.GET.getlist('ingredientes[]')
    nombre = request.GET['nombre']
    precio = request.GET['precio']
    producto = Producto(nombre = nombre, precio = precio, carta = carta)
    print "Guardé el producto"
    producto.save()
    print "Guardé el producto"
    for i in ingredientes:
        ing = Ingrediente.objects.get(pk=i)
        producto.ingredientes.add(ing)
        print "Añadi el ingrediente"
        producto.save()
        print "guardé el producto en el for"
    data = "El producto ha sido creado con éxito"
    return HttpResponse(data, content_type='text/plain')