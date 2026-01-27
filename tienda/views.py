from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView, TemplateView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CompraForm
from django.contrib import messages
from django.db.models import Sum

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
    
class ComprarProducto (ListView):
    model = Producto
    template_name = 'tienda/compra_listado.html'
    context_object_name = 'productos'
    
    def get_queryset(self):
        query =  super().get_queryset()
        nombre = self.request.GET.get('input_nombre')
        if nombre:
            query = query.filter(nombre__icontains = nombre)
        return query
    
class CheckoutViews(View):
    def get(self, request, pk):
        producto = Producto.objects.get(pk = pk)
        form = CompraForm()
        return render(request, "app/checkout.html", {"producto":producto, "form":form})
                
    def post (self, request, pk):
        producto = Producto.objects.get(pk = pk)
        form = CompraForm((request.POST))
        if form.is_valid():
            unidades = form.cleaned_data['unidades']
            
            if producto.unidades < unidades:
                messages.error(request, "No hay suficiente stock")
            
            else:
                #Agregamos la compra
                usuario = request.user
                importe = unidades * producto.precio

                if usuario.saldo >= importe:
                    Compra.objects.create(usuario = request.user, producto = producto,
                                        unidades = unidades, importe = importe, iva = 0.21)
                    #testamos las unidades del stock/producto
                    producto.unidades -= unidades
                    producto.save()
                    
                    usuario.saldo -= importe
                    usuario.save()
                    messages.success(request, "Guardado correctamente")
        return redirect("compra_listado")
    
class Perfil(TemplateView):
    template_name = 'tienda/perfil.html'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto ['compras'] = Compra.objects.filter(usuario = self.request.user)
        return contexto
    
def informes(request):
    topclientes = Compra.objects.annotate(total_gastado = Sum('compras_importe')).order_by('-total_gastado')[:10]
    return render(request, 'tienda/informes.html', {Cliente})