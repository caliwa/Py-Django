from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from Empleados.forms import Empleados_form, ContactoEmer_form, SegSocial_form
from Empleados.models import Empleados, ContactoEmergencia, SeguridadSocial
from django.contrib.auth.decorators import login_required


#empleado
@login_required
def empleado_create(request):
    model = 'Empleados'
    if request.method == 'POST':
        form = Empleados_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar/')
    else:
        form = Empleados_form()
    return render(request, 'create.html', {"form":form, "model":model})
    #else:
    #    return HttpResponse('EL SERVIDOR ESTÁ ENVIANDO INFORMACIÓN COMO GET')
    
@login_required
def empleado_list(request):
    model = Empleados.objects.all()
    return render(request, 'list.html', {"model": model}) 

@login_required
def empleado_delete(request, pk):
    model = Empleados.objects.get(id=pk)
    model.delete()
    return redirect('/listar/')

@login_required
def empleado_update(request, pk):
    model = Empleados.objects.get(id=pk)
    if request.method == 'POST':
        form = Empleados_form(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('/listar/')
    else:
        form = Empleados_form(instance=model)
    return render(request, 'create.html', {"form":form, "model":model})

#contacto de emergencia
@login_required
def emergency_create(request):
    model = 'Contacto de Emergencia'
    if request.method == 'POST':
        form = ContactoEmer_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar/')
    else:
        form = ContactoEmer_form()
    return render(request, 'create.html', {"form":form, "model":model})
'''
@login_required
def emergency_create(request, pk):
    model = 'Contacto de Emergencia'
    if request.method == 'POST':
        n = request.POST.get("nombres")
        a = request.POST.get("apellidos")
        d = request.POST.get("celular")
        b = request.POST.get("parentesco")
        p = Empleados.objects.get(id=pk)
        form = ContactoEmergencia(contacto_emergencia = p, nombres = n, apellidos = a, celular = d, parentesco = b)
        form.save()
        return redirect('/listar/')
    else:
        form = ContactoEmer_form()
    return render(request, 'create.html', {"form":form, "model":model})
'''
@login_required
def segsocial_create(request):
    model = 'Seguridad Social'
    if request.method == 'POST':
        form = SegSocial_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar/')
    else:
        form = SegSocial_form()
    return render(request, 'create.html', {"form":form, "model":model})
'''
@login_required
def segsocial_create(request, pk):
    model = 'Seguridad Social'
    if request.method == 'POST':
        n = request.POST.get("eps")
        a = request.POST.get("afp")
        d = request.POST.get("ccf")
        b = request.POST.get("arl")
        p = Empleados.objects.get(id=pk)
        form = SeguridadSocial(empleado = p, eps = n, afp = a, ccf = d, arl = b)
        form.save()
        return redirect('/listar/')
    else:
        form = SegSocial_form()
    return render(request, 'create.html', {"form":form, "model":model})
'''