# Generated by Django 4.2.1 on 2023-08-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Slug')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('imagen', models.ImageField(upload_to='blogs/%Y/%m/', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Requerimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Numero de requerimiento')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blogs/requerimientos/%Y/%m/', verbose_name='Mockup requerimiento')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre requerimiento')),
                ('hecho', models.BooleanField(default=False, verbose_name='Hecho')),
            ],
            options={
                'verbose_name': 'Requerimiento',
                'verbose_name_plural': 'Requerimientos',
            },
        ),
    ]
