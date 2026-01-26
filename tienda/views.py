from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class CrearProducto(CreateView):
    model = Producto
    template_name = 'tienda/producto_crear.html'
    fields = '__all__'
    success_url = reverse_lazy("listado")

class ListadoProducto (ListView):
    model = Producto
    template_name = 'tienda/producto_listado.html'
    context_object_name = 'productos'
    
class DetalleProducto (DetailView):
    model = Producto
    template_name = 'tienda/producto_detalle.html'
    
class EditarProducto (UpdateView):
    model = Producto
    template_name = 'tienda/producto_editar.html'
    fields = '__all__'
    success_url = reverse_lazy("listado")

class BorrarProducto (DeleteView):
    model = Producto
    template_name = 'tienda/prodructo_borrar.html'
    success_url = reverse_lazy("listado")