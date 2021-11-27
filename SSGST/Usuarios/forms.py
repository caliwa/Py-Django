from django import forms
from django.forms.fields import CharField


class LoginForms(forms.Form):
    usuario = CharField(min_length = 1, label= 'Usuario ')
    contrasena = CharField(min_length = 1, widget=forms.PasswordInput(), label= 'Contraseña ')
