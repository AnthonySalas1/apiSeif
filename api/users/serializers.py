
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import User, Unidad


class UserSerializer(serializers.Serializer):
    dni = serializers.IntegerField()
    passwd = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100, allow_null=True)
    lastname = serializers.CharField(max_length=100, allow_null=True)
    age = serializers.IntegerField(allow_null=True)
    category = serializers.ChoiceField(allow_null=True,
        choices=User.CATEGORIES_CHOICES)
    imagen = serializers.CharField(allow_null=True, max_length=200)
    email = serializers.EmailField(max_length=40)
    release_date = serializers.DateField(allow_null=True)
    

class UnidadSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=100)
    rutas = serializers.CharField(max_length=200)
    partida = serializers.CharField(max_length=200)
    llegada = serializers.CharField(max_length=200)
    contacto = serializers.IntegerField()
    imagen = serializers.CharField(max_length=200)
    link = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new  instance, given the validated data.
        """
        return User.objects.create(**validated_data)



    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.dni = validated_data.get('dni', instance.dni)
        instance.passwd = validated_data.get('passwd', instance.passwd)
        instance.name = validated_data.get('name', instance.name)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.age = validated_data.get('age', instance.age)
        instance.category = validated_data.get('category', instance.category)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.email = validated_data.get('email', instance.email)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance


    def create(self, validated_data):
        """
        Create and return a new  instance, given the validated data.
        """
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.titulo = validated_data.get('lastname', instance.titulo)
        instance.rutas = validated_data.get('age', instance.rutas)
        instance.partida = validated_data.get('partida', instance.partida)
        instance.llegada = validated_data.get('llegada', instance.llegada)
        instance.contacto = validated_data.get('contacto', instance.contacto)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.link = validated_data.get('link', instance.link)
        instance.release_date = validated_data.get(
            'release_date', instance.release_date)
        instance.save()
        return instance
