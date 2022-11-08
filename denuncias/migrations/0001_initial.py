# Generated by Django 4.0.1 on 2022-11-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id_denuncia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_denunciante', models.CharField(max_length=60)),
                ('apellido_denunciante', models.CharField(max_length=60)),
                ('rut_denunciante', models.CharField(max_length=14)),
                ('situacion', models.CharField(max_length=254)),
                ('direccion', models.CharField(max_length=254)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_delito', models.DateTimeField()),
            ],
        ),
    ]
