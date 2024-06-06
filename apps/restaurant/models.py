from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre}'