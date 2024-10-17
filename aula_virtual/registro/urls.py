from django.urls import path
from . import views

urlpatterns = [
    path('motivos-clase/', views.motivo_clase_list, name='motivo-clase-list'),
    path('motivos-clase/<int:pk>/', views.motivo_clase_detail, name='motivo-clase-detail'),
    path('registros-clase/', views.registro_clase_list, name='registro-clase-list'),
    path('registros-clase/<int:pk>/', views.registro_clase_detail, name='registro-clase-detail'),
]
