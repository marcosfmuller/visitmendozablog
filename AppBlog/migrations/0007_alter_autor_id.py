# Generated by Django 4.1.4 on 2023-01-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_alter_autor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
