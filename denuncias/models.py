from django.db import models

# Create your models here.

class Denuncia(models.Model):
    id_denuncia = models.AutoField(primary_key=True)
    nombre_denunciante = models.CharField(max_length=60)
    apellido_denunciante = models.CharField(max_length=60)
    rut_denunciante = models.CharField(max_length=14)