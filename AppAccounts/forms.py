from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:"" for k in fields}

class UserEditForm(forms.ModelForm):
    email=forms.EmailField()
    password1=forms.CharField(label='Nueva Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirme Contraseña',widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')

    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        help_texts={k:"" for k in fields}

class AvatarForm(forms.ModelForm):
    imagen=forms.ImageField(label='Imagen')



