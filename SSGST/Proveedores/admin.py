from django.contrib import admin
from Proveedores.models import *

# Register your models here.
admin.site.register(Proveedores)
admin.site.register(ElementosProteccionPersonal)
admin.site.register(ElementosProveedor)

class Proveedores (admin.ModelAdmin):
    list_display = ('nombre', 'nit', 'certificado_arl', 'autorizado', 'seguridad_social', 'telefono1', 'telefono2', 'email', 'tipo_empresa')
    search_fields = ('nombre')
    
class ElementosProteccionPersonal(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre')
    
class ElementosProveedor(admin.ModelAdmin):
    list_display = ('proveedor', 'elemento', 'ficha_seguridad')
    search_fields = ('proveedor')