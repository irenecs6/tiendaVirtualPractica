from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('tienda/admin/productos/crear', CrearProducto.as_view(), name='crear'),
    path('tienda/admin/productos/listar', ListadoProducto.as_view(), name='listar'),
    path('tienda/admin/productos/detalle/<int:pk>', DetalleProducto.as_view(), name='detalle'),
    path('tienda/admin/productos/editar/<int:pk>', EditarProducto.as_view(), name='editar'),
    path('tienda/admin/productos/borrar/<int:pk>', BorrarProducto.as_view(), name='borrar'),

]
