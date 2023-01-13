from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            #messages.success(request,f'Usuario creado: {username}!')
            #return redirect('AppBlog:home')
            return render(request, 'index.html', {"mensaje":"Usuario {username} creado correctamente!"})
        else:
            return render(request, 'register.html', {"form":form, "mensaje":"Error al crear usuario"})
    else:
        form=RegistroUsuarioForm()    
    return render(request, 'register.html', {"form":form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect("AppBlog:index")
            else:
                return render(request, 'login.html', {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, 'login.html', {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()    
    return render(request, 'login.html', {"form":form})

@login_required
def editar_perfil(request):
    if request.method=="POST":
        form=UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('AppBlog:index')
    else:
        form=UserEditForm(instance=request.user)    
    return render(request, 'profile.html', {"form":form})