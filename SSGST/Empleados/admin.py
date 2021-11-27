from django.contrib import admin
from Empleados.models import Empleados, Cargo, Area

admin.site.register(Empleados)
admin.site.register(Cargo)
admin.site.register(Area)