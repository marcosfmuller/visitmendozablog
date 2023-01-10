from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la Categoría', max_length=100, null = False, blank = False)
    status = models.BooleanField('Categoría Activa / Categoría No Activa', default=True)
    published = models.DateField('Fecha de Creación', auto_now_add=True, auto_now=False)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self):
        return self.name

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre del Autor', max_length=100, null = False, blank = False)
    surname = models.CharField('Apellido del Autor', max_length=100, null = False, blank = False)
    facebook = models.URLField('Facebook', max_length=100, null = True, blank = True)
    twitter = models.URLField('Twitter', max_length=100, null = True, blank = True)
    instagram = models.URLField('Instagram', max_length=100, null = True, blank = True)
    web = models.URLField('Web', max_length=100, null = True, blank = True)
    email = models.EmailField('Email', max_length=100, null = False, blank = False)
    status = models.BooleanField('Autor Activo / Autor No Activo', default=True)
    published = models.DateTimeField('Fecha de Creación', auto_now_add=True, auto_now=False)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self):
        return "{0} {1}".format(self.name, self.surname)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Nombre del Post', max_length=100, null = False, blank = False)
    slug = models.CharField('Slug', max_length=100, null = False, blank = False)
    description = models.CharField('Descripción', max_length=100, null = True, blank = True)
    image = models.URLField(max_length=200, null = False, blank = False)
    autor = models.ForeignKey(Autor, max_length=100, verbose_name='Autor', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Categoría', on_delete=models.CASCADE)
    status = models.BooleanField('Post Activo / Post No Activo', default=True)
    content = RichTextField()
    published = models.DateField('Fecha de Creación', auto_now_add=True)
    updated = models.DateField('Fecha de Modificacion', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title

class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Titulo', max_length=100, null = False, blank = False)
    description = models.CharField('Descripción', max_length=100, null = True, blank = True)
    image = models.URLField(max_length=200, null = False, blank = False)
    content = RichTextField()
    status = models.BooleanField('Activo / No Activo', default=True)
    published = models.DateField('Fecha de Creación', auto_now_add=True)
    updated = models.DateField('Fecha de Modificacion', auto_now=True)

    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de'
        
    def __str__(self):
        return self.title