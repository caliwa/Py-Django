"""SSGST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Empleados.views import empleado_create, empleado_list, empleado_delete, empleado_update, emergency_create, segsocial_create
from Usuarios.views import LoginView, Logout_view 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls, name="Admin"),
    path('logout/', Logout_view, name="Logout_view"),
    path('empleados/new', empleado_create, name='Empleado'),
    path('contacto_emergencia/new', emergency_create, name='Emergency'),
    path('seg_emergencia/new', segsocial_create, name='Seg_Social'),
    path('listar/', empleado_list, name="Listar"),
    path('borrar/<int:pk>', empleado_delete, name="Delete"),
    path('update/<int:pk>', empleado_update, name="Update"),
    path('', LoginView, name="login")
]
