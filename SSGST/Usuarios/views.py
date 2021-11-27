from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from Usuarios.forms import LoginForms
from django.contrib.auth import authenticate, login, logout

def LoginView(request):
    if request.method == 'POST':
        X = LoginForms(request.POST)
        if X.is_valid():
            User = request.POST.get('usuario')
            Pass = request.POST.get('contrasena')
            Aut = authenticate(username = User, password = Pass)
            if Aut is not None:
                login(request, Aut)
                return redirect('/listar/')
            else:
                return HttpResponse("Usuario no encontrado/Contraseña incorrecta")
    else:
        X = LoginForms
        return render(request, "login.html", {"X": X})
        
def Logout_view(request):
    logout(request)
    return redirect('login')