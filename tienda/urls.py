from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('productos/crear', CrearProducto.as_view(), name='crear'),
    path('productos/listar', ListadoProducto.as_view(), name='listar'),
    path('productos/detalle/<int:pk>', DetalleProducto.as_view(), name='detalle'),
    path('productos/editar/<int:pk>', EditarProducto.as_view(), name='editar'),
    path('productos/borrar/<int:pk>', BorrarProducto.as_view(), name='borrar'),

]
