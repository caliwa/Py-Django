from django.db import models
from Empleados.models import Empleados
from django.db.models.deletion import CASCADE

class TiposdeDocumento(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateField(auto_now_add = True)
    def __str__ (self):
        return f'{self.nombre}'
    
class DocumentacionEmpleado(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete = CASCADE)
    tipo_documento = models.ForeignKey(TiposdeDocumento, on_delete = CASCADE)
    archivo = models.FileField(upload_to='SSGST/documentos')
    fecha_vencimiento = models.DateField(auto_now_add = True)
    observaciones = models.TextField(max_length = 300)
    fecha_creacion = models.DateField(auto_now_add = True)
    
class DocumentacionEmpresa(models.Model):
    titulo = models.CharField(max_length = 25)
    tipo_documento = models.ForeignKey(TiposdeDocumento, on_delete = CASCADE)
    descripcion = models.TextField(max_length=50)
    firma = models.CharField(max_length = 30)
    fecha_vencimiento = models.DateField(auto_now_add = True)
    observaciones = models.TextField(max_length = 300)
    fecha_creacion = models.DateField(auto_now_add = True)

class ConfiguracionEmpresa(models.Model):
    nombre_empresa = models.CharField(max_length=30)
    nit = models.CharField(max_length=11)
    longitud = models.CharField(max_length=25)
    latitud = models.CharField(max_length=25)
    actividad_economica = models.CharField(max_length=30)
    nivel_riesgo = models.CharField(max_length=30)
    cantidad_trabajadores = models.PositiveBigIntegerField()
    naturaleza_juridica = models.CharField(max_length=30)
    telefono1 = models.BigIntegerField()
    telefono2 = models.BigIntegerField(blank = True, null = True)
    telefono3 = models.BigIntegerField(blank = True, null = True)
    direccion = models.CharField(max_length=25)
    email = models.EmailField()
    pagina_web = models.URLField()
    tipo_empresa = models.CharField(max_length=20)
    fecha_creacion = models.DateField(auto_now_add = True)
