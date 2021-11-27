from django import forms
from Empleados.models import Empleados, ContactoEmergencia, SeguridadSocial

class Empleados_form(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type':'date'}, format = ('%Y-%m-%d')),
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}, format = ('%Y-%m-%d')),
            'fecha_retiro': forms.DateInput(attrs={'type':'date'}, format = ('%Y-%m-%d')),
            }
        
        
class ContactoEmer_form(forms.ModelForm):
    class Meta:
        model = ContactoEmergencia
        fields = '__all__'
    
class SegSocial_form(forms.ModelForm):
    class Meta:
        model = SeguridadSocial
        fields = '__all__'