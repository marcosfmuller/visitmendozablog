# Generated by Django 4.1.4 on 2023-01-03 05:32

import AppBlog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0009_post_slug_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=100, verbose_name=AppBlog.models.Autor),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=100, verbose_name='Slug'),
        ),
    ]
