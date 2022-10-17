from atexit import register
from django.contrib import admin
from .models import Unidad, User

admin.site.register(User)
admin.site.register(Unidad)


# Register your models here.
