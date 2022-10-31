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

    dni = models.IntegerField(blank=False)
    passwd = models.CharField(max_length=30, unique=True)
    name = models.CharField(null=True, blank=True, max_length=100)
    lastname = models.CharField(null=True,max_length=100, blank=True)
    age = models.IntegerField(null=True,blank=True)
    category = models.CharField(null=True, max_length=1, blank=True, choices=CATEGORIES_CHOICES)
    imagen = models.URLField(null=True, max_length=200, blank=True)
    email = models.EmailField(unique=True,
        max_length=40)
    release_date = models.DateField('date published', null=True, blank=True)

    def __str__(self):
        return str(self.name) + " " + str(self.dni)

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

    
