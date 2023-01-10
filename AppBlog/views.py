from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):
    posts = Post.objects.filter(status=True)
    return render(request, 'index.html', {'posts':posts})

def detailpost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', {'post':post})

def about(request):
    about = About.objects.get(id=1)
    return render(request, 'about.html', {'about':about})

def gastronomy(request):
    posts = Post.objects.filter(
        status=True, 
        category= Category.objects.get(name='Gastronomía')
    )
    return render(request, 'gastronomy.html', {'posts':posts})

def hotels(request):
    posts = Post.objects.filter(
        status=True,
        category= Category.objects.get(name='Hotelería')
    )
    return render(request, 'hotels.html' , {'posts':posts})

def activities(request):
    posts = Post.objects.filter(
        status=True,
        category= Category.objects.get(name='Actividades')
    )
    return render(request, 'activities.html', {'posts':posts})

