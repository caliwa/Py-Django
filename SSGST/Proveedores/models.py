from django.db import models

from django.db.models.deletion import CASCADE

# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField(max_length=20)
    nit = models.CharField(max_length=11)
    certificado_arl = models.FileField(upload_to='SSGST/documentos')
    autorizado = models.BooleanField()
    seguridad_social = models.FileField(upload_to='SSGST/documentos')
    telefono1 = models.PositiveBigIntegerField()
    telefono2 = models.PositiveBigIntegerField(null = True, blank = True)
    email = models.EmailField()
    tipo_empresa = models.CharField(max_length=20)
    fecha_creacion = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.nombre
    
class ElementosProteccionPersonal(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_creacion = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.nombre

class ElementosProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=CASCADE)
    elemento = models.ForeignKey(ElementosProteccionPersonal, on_delete=CASCADE)
    ficha_seguridad = models.FileField(upload_to='SSGST/documentos')
    fecha_creacion = models.DateField(auto_now_add = True)
