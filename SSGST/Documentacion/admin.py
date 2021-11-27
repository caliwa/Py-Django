from django.contrib import admin
from Documentacion.models import TiposdeDocumento, DocumentacionEmpleado, DocumentacionEmpresa, ConfiguracionEmpresa

admin.site.register(TiposdeDocumento)
admin.site.register(DocumentacionEmpleado)
admin.site.register(DocumentacionEmpresa)
admin.site.register(ConfiguracionEmpresa)

class TiposdeDocumento(admin.ModelAdmin):
    list_display = ("nombre", "fecha_creacion")
    search_fields = ("nombre")

class DocumentacionEmpleado(admin.ModelAdmin):
    list_display = ("empleado", "tipo_documento", "fecha_vencimiento", "fecha_creacion", "observaciones")
    search_fields = ("empleado", "tipo_documento")
    
class DocumentacionEmpleado(admin.ModelAdmin):
    list_display = ("titulo", "tipo_documento", "descripcion", "firma", "fecha_vencimiento", "observaciones", "fecha_creacion")
    search_fields = ("titulo", "tipo_documento")

class ConfiguracionEmpresa(admin.ModelAdmin):
    list_display = ("nombre_empresa", "nit", "longitud", "latitud", "actividad_economica", "nivel_riesgo", "cantidad_trabajadores", "naturaleza_juridica", "telefono1", "direccion", "email", "pagina_web")