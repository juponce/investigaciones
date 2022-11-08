from django.db import models

# Create your models here.

class Denuncia(models.Model):
    id_denuncia = models.AutoField(primary_key=True)
    nombre_denunciante = models.CharField(max_length=60)
    apellido_denunciante = models.CharField(max_length=60)
    rut_denunciante = models.CharField(max_length=14)
    situacion = models.CharField(max_length=254)
    descrpción_sospechoso = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=254)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_delito = models.DateField()