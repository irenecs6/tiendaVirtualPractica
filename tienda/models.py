from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class IVAChoices(models.TextChoices):
    IVA21 = "21", "21%"
    IVA10 = "10", "10%"
    IVA4 = "4", "4%"

class Usuario (AbstractUser):
    vip = models.BooleanField(default=False)
    saldo = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, blank=True, null=True)
    
    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    
    
class Marca (models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name_plural = 'Marcas'
        


class Producto (models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    unidades = models.IntegerField(default=0)
    precio = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    vip = models.BooleanField(default=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name_plural = 'Productos'
        
        
            
class Compra (models.Model):
    fecha = models.DateTimeField(auto_now=True) #Auto_now para que coja la fecha del dia actual
    unidades = models.IntegerField(default=0)
    importe = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    iva = models.CharField(max_length=2, choices=IVAChoices, default=IVAChoices.IVA21)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Compra {self.producto.nombre} de {self.usuario.username}'
    
    class Meta:
        verbose_name_plural = 'Compras'