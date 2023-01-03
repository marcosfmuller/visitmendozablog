from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la Categoría', max_length=100, null = False, blank = False)
    status = models.BooleanField('Categoría Activa / Categoría No Activa', default=True)
    published = models.DateTimeField('Fecha de Creación', auto_now_add=True, auto_now=False)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Nombre del Post', max_length=100, null = False, blank = False)
    status = models.BooleanField('Post Activo / Post No Activa', default=True)
    content = models.TextField()
    published = models.DateTimeField('Fecha de Creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de Modificacion', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title

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
        return "{0},{1}".format(self.name, self.surname)