# Generated by Django 4.1.4 on 2023-01-10 05:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0015_alter_post_autor_alter_post_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción')),
                ('image', models.URLField()),
                ('content', ckeditor.fields.RichTextField()),
                ('status', models.BooleanField(default=True, verbose_name='Post Activo / Post No Activo')),
                ('published', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
            ],
            options={
                'verbose_name': 'Acerca de',
                'verbose_name_plural': 'Acerca de',
            },
        ),
    ]