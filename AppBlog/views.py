from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import PostForm
from datetime import datetime
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    quertyset = request.GET.get('buscar')
    posts = Post.objects.filter(status=True)
    if quertyset:
        posts = Post.objects.filter(
            Q(title__icontains=quertyset) |
            Q(description__icontains=quertyset)
            ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts':posts})

@login_required
def detailpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post':post})

def about(request):
    about = About.objects.get(id=1)
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
    return render(request, 'hotels.html' , {'posts':posts})

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
    return render(request, 'activities.html', {'posts':posts})

"""def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            return redirect('post', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'newpost.html', {'form':form})
"""

class createPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'newpost.html'
    #fields = ['title', 'slug', 'description', 'category']
    success_url = reverse_lazy('index')

