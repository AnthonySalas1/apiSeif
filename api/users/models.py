from pyexpat import model
from ssl import Options
from sys import maxsize
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.db import models
from django.forms import EmailField

class User(models.Model):

    Conductor = 'C'
    Usuario = 'U'

    CATEGORIES_CHOICES = (
        (Conductor, 'C'),
        (Usuario, 'U')
    )

    dni = models.IntegerField(default='12345678')
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    category = models.CharField(max_length=1, choices=CATEGORIES_CHOICES)
    imagen = models.URLField(max_length=200, blank=True, default='link-image')
    email = models.EmailField(max_length= 40, default="example@any.com")
    release_date = models.DateField('date published')

    def __str__(self) -> str:
        return self.name

class Unidad(models.Model):
    titulo = models.CharField(max_length=40)
    rutas = models.CharField(max_length=200)
    partida = models.CharField(max_length=200)
    llegada = models.CharField(max_length=200)
    contacto = models.IntegerField(null=True)
    imagen = models.URLField(max_length=200, default='link-image', blank=True)
    link = models.URLField(max_length=200, default='link website', blank=True)
    release_date = models.DateTimeField('date published')
    
    def __str__(self) -> str:
        return self.titulo

    
