from django.db import models

# Create your models here.


class limpieza(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precios = models.CharField(max_length=50)
