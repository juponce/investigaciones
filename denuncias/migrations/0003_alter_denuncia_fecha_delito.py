# Generated by Django 4.0.1 on 2022-11-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0002_denuncia_descrpción_sospechoso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='fecha_delito',
            field=models.DateField(),
        ),
    ]
