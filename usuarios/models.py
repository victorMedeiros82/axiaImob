# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPOS = (
        ('PROPRIETARIO', 'Proprietário'),
        ('INQUILINO', 'Inquilino'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS)
    # Campos que podem ser comuns ou específicos
    cpf_cnpj = models.CharField(max_length=18, blank=True)
    telefone = models.CharField(max_length=15, blank=True)