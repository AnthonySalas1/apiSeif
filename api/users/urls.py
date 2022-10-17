from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('users', views.user_list, name='user_list'),
    path('users/<int:pk>',views.user_detail, name='user_detail'),
    path('unidades', views.unidad_list, name='unidad_list'),
    path('unidades/<int:pk>', views.unidad_detail, name='unidad_detail'),
]