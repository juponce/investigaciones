from django.db import models

# Create your models here.


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=60)


class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=60)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=60)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)


class Ruta(models.Model):
    id_ruta = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=60)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class HorarioTransporte(models.Model):
    id_horario = models.AutoField(primary_key=True)
    horaInicio = models.TimeField()
    horaFinal = models.TimeField()
    horarioEspecial = models.TimeField(null=True, blank=True)
    dia = models.CharField(max_length=60)