# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.views import generic
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from drinking.models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q


# class HomeView(generic.TemplateView):
#     template_name = "drinking/home.html"

def home(request):
    user = request.user
    if user.is_authenticated():
        profile = user.profile
    return render(request, 'drinking/home.html')

# @permission_required('polls.can_vote')
# def admin_login(request):


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

    return render(request, 'drinking/mylocal.html',
                  { 'local': local, 'carta' : carta})

def anadirElementoCarta(request):
    local = request.user.admin.local
    carta = Carta.objects.get(local = local)
    if request.method == 'POST':
        q_producto = request.POST['producto']
        producto = Producto.objects.get(id=q_producto)
        precio = request.POST['precio']
        CartaProducto.objects.create(producto = producto, precio = precio, carta = carta)

    productos_de_carta = CartaProducto.objects.filter(carta = carta)

    # return render(request, 'drinking/mylocal.html', { 'local': local, 'carta' : carta, 'productos' : productos})
    return render(request,'drinking/mylocal.html',
                       { 'local':local, 'carta':carta,
                       'cartaProductos':productos_de_carta})


def test(request):
    return render(request, 'drinking/testadmin.html')
