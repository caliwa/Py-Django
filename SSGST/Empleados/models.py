from django.db import models
from django.db.models.deletion import CASCADE

class Area(models.Model):
    area = models.CharField(max_length=15)
    
class Cargo(models.Model):
    id_area = models.ForeignKey(Area, on_delete=CASCADE)
    cargo = models.CharField(max_length=20)
    def __str__(self):
        return (self.cargo)
    
class Empleados(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cargo = models.ForeignKey(Cargo, on_delete=CASCADE)
    
    LVL_ESTUDIO = [
        ('Primaria', 'Primaria'),
        ('Bachillerato', 'Bachillerato'),
        ('Técnico', 'Técnico'),
        ('Tecnológico', 'Tecnológico'),
        ('Universitario', 'Universitario'),
        ('Especialización', 'Especialización'),
        ('Maestría', 'Maestría'),
        ('Doctorado', 'Doctorado'),
    ]   

    lvl_estudio = models.CharField(max_length=20, null= True, blank=True, choices = LVL_ESTUDIO)
    fecha_ingreso = models.DateField(null= True, blank=True)
    fecha_nacimiento = models.DateField(null= True, blank=True)
    edad = models.PositiveSmallIntegerField(null= True, blank=True)
    cedula = models.CharField(max_length=12)
    
    GENERO = [
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTRO')
    ]

    genero = models.CharField(max_length=20, null= True, blank=True, choices = GENERO)
    
    SANGRE = [('O+', 'O+'),
              ('O-', 'O-'),
              ('A+', 'A+'),
              ('A-', 'A-'),
              ('B-', 'B-'),
              ('B+', 'B+'),
              ('AB-', 'AB-'),
              ('AB+', 'AB+')]
    
    sangre = models.CharField(max_length=20, null= True, blank=True, choices = SANGRE)
    
    turno_trabajo = models.CharField(max_length=12)
    telefono_fijo = models.PositiveIntegerField(null= True, blank=True)
    celular = models.PositiveIntegerField(null= True, blank=True)
    email = models.EmailField(null= True, blank=True)
    direccion = models.CharField(max_length=30, null= True, blank=True)
    municipio = models.CharField(max_length=30, null= True, blank=True)
    estrato = models.PositiveSmallIntegerField(help_text="De 1 a 6", null= True, blank=True)
    
    ETNIAS = [('Blanco', 'Blanco'),
              ('Mestizo', 'Mestizo'),
              ('Afrocolombiano', 'Afrocolombiano'),
              ('Mulato', 'Mulato'),
              ('Indígena', 'Indígena')]
    
    etnias = models.CharField(max_length=20, null= True, blank=True, choices = ETNIAS)
    
    CIVIL = [('Soltero', 'Soltero'),
              ('Casado', 'Casado'),
              ('Separado', 'Separado'),
              ('Unión Libre', 'Unión Libre'),
              ('Viudo', 'Viudo')]
    
    civil = models.CharField(max_length=20, null= True, blank=True, choices = CIVIL)
    hijos = models.PositiveSmallIntegerField(null= True, blank=True)
    tipo_contrato = models.CharField(max_length=30, null= True, blank=True)
    enfermedad = models.CharField(max_length=30, null=True, blank=True, help_text="Si no sufre ninguna enfermedad, dejar campo en blanco")
    medicamentos = models.CharField(max_length=30, null=True, blank=True)
    induccion = models.BooleanField(null= True, blank=True)
    vacuna = models.BooleanField(null= True, blank=True)
    carnet = models.FileField(null= True, blank=True)
    estado_actividad = models.BooleanField(null= True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, null= True, blank=True)
    fecha_retiro = models.DateField(null= True, blank=True)
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class SeguridadSocial(models.Model):
    empleado = models.OneToOneField(Empleados, on_delete=CASCADE)
    eps = models.CharField(max_length=20)
    afp = models.CharField(max_length=20)
    ccf = models.CharField(max_length=20)
    arl = models.CharField(max_length=20)
    
class ContactoEmergencia(models.Model):
    contacto_emergencia = models.OneToOneField(Empleados, on_delete=CASCADE, primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    celular = models.PositiveIntegerField(null= True, blank=True)
    parentesco = models.CharField(max_length=30, null=True, blank=True)
    