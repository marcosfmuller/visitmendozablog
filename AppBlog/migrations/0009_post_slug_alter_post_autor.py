# Generated by Django 4.1.4 on 2023-01-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0008_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=100, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=100),
        ),
    ]
