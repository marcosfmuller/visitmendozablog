from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import *
from AppAccounts.models import Avatar
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="media/avatars/transparent-default-avatar.png"
    return imagen

def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(status=True)
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset)
            ).distinct()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if request.user.is_authenticated:
        return render(request, 'index.html', {'posts':posts, 'imagen':obtenerAvatar(request)})
    else:
        return render(request, 'index.html', {'posts':posts})
    
          

@login_required
def detailpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post':post, 'imagen':obtenerAvatar(request)})

def about(request):
    about = About.objects.get(id=1)
    if request.user.is_authenticated:
        return render(request, 'about.html', {'about':about, 'imagen':obtenerAvatar(request)})
    else:
        return render(request, 'about.html', {'about':about})    

def gastronomy(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        status=True, 
        category= Category.objects.get(name__iexact = 'Gastronomía')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            status=True,
            category = Category.objects.get(name__iexact = 'Gastronomía')
            ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if request.user.is_authenticated:
        return render(request, 'gastronomy.html', {'posts':posts, 'imagen':obtenerAvatar(request)})
    else:
        return render(request, 'gastronomy.html', {'posts':posts})

def hotels(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        status=True,
        category= Category.objects.get(name__iexact = 'Hotelería')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            status=True,
            category = Category.objects.get(name__iexact = 'Hotelería')
            ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if request.user.is_authenticated:
        return render(request, 'hotels.html', {'posts':posts, 'imagen':obtenerAvatar(request)})
    else:
        return render(request, 'hotels.html', {'posts':posts})
    
def activities(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        status=True,
        category= Category.objects.get(name__iexact = 'Actividades')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            status=True,
            category = Category.objects.get(name__iexact = 'Actividades')
            ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if request.user.is_authenticated:
        return render(request, 'activities.html', {'posts':posts, 'imagen':obtenerAvatar(request)})
    else:
        return render(request, 'activities.html', {'posts':posts})

class createPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostAdminForm
    template_name = 'newpost.html'
    success_url = reverse_lazy('AppBlog:index')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'postoptions.html'
    context_object_name = 'posts'

class updatePost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostAdminForm
    template_name = 'postedit.html'
    success_url = reverse_lazy('AppBlog:index')

class deletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'postdelete.html'
    success_url = reverse_lazy('AppBlog:index')

