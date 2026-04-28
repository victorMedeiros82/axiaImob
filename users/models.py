from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPO_CHOICES = (
        ('socio', 'Sócio'),
        ('analista', 'Analista'),
        ('gestor', 'Gestor'),
        ('administrador', 'Administrador'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)