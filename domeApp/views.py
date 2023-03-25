from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import limpieza
from django.contrib import messages

def inscribirse(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'inscribrise.html ', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'inscribrise.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def iniciarsesion(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/perfil')  # profile
        else:
            msg = 'Usuario o contraseña incorrecta'
            form = AuthenticationForm(request.POST)
            return render(request, 'acceso.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'acceso.html', {'form': form})


def perfil(request):
    return render(request, 'perfil.html')


def salir(request):
    logout(request)
    return redirect('/')

##############################################################

def homedef(request):
    limpiezaListados = limpieza.objects.all()
    messages.success(request, '¡limpieza listados!')
    return render(request, "gestionlimpieza.html", {"cursos": limpiezaListados})


def registrarlimpieza(request):
    codigo = request.POST['Codigo']
    nombre = request.POST['Nombre']
    precios = request.POST['numprecios']

    curso = limpieza.objects.create(
        codigo=codigo, nombre=nombre, precios=precios)
    messages.success(request, '¡Registrado!')
    return redirect('/')


def edicionlimpieza(request, codigo):
    curso = limpieza.objects.get(codigo=codigo)
    return render(request, "edicionlimpieza.html", {"curso": curso})


def editarlimpieza(request):
    codigo = request.POST['Codigo']
    nombre = request.POST['Nombre']
    precios = request.POST['numprecios']

    curso = limpieza.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.precios = precios
    curso.save()

    messages.success(request, '¡Registro actualizado!')

    return redirect('/')


def eliminarlimpieza(request, codigo):
    curso = limpieza.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Registro eliminado!')

    return redirect('/')