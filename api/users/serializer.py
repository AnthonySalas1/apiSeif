from rest_framework import serializers
from .models import Unidad, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = "__all__"




