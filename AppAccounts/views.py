from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Avatar
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import *


# Create your views here.

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="media/avatars/transparent-default-avatar.png"
    return imagen

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, 'login.html', {"mensaje":f"Usuario {username} creado correctamente!"})
        else:
            return render(request, 'register.html', {"form":form, "mensaje":"Error al crear usuario"})
    else:
        form=RegistroUsuarioForm()    
    return render(request, 'register.html', {"form":form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            usuario=authenticate(username = username, password = password)
            if usuario is not None:
                login(request, usuario)
                return redirect("AppBlog:index")
            else:
                return render(request, 'login.html', {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, 'login.html', {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()    
    return render(request, 'login.html', {"form":form})

@login_required
def panelctrl(request):
    return render(request, 'panelctrl.html', {'imagen':obtenerAvatar(request)})

@login_required
def editar_perfil(request):
    if request.method=="POST":
        form=UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'panelctrl.html', {"form":form, "mensaje":"Perfil actualizado correctamente"})
    else:
        form=UserEditForm(instance=request.user)    
    return render(request, 'profile.html', {"form":form, 'imagen':obtenerAvatar(request)})

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return redirect('AppBlog:index')
        else:
            return render(request, 'avataradd.html', {"formulario":form, "usuario":request.user})
    else:
        form=AvatarForm()    
        return render(request, 'avataradd.html', {"formulario":form, "usuario":request.user, 'imagen':obtenerAvatar(request)})

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'userlist.html'
   
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'useredit.html'
    fields = ['email', 'first_name', 'last_name']
    success_url = reverse_lazy('AppAccounts:userlist')
    
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'userdelete.html'
    success_url = reverse_lazy('AppAccounts:userlist')
