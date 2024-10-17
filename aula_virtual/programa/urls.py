from django.urls import path
from . import views

urlpatterns = [
    path('programas/', views.programa_list, name='programa-list'),
    path('programas/<int:pk>/', views.programa_detail, name='programa-detail'),
    path('hojas-de-vida/', views.hoja_de_vida_list, name='hoja-de-vida-list'),
    path('hojas-de-vida/<int:pk>/', views.hoja_de_vida_detail, name='hoja-de-vida-detail'),
    path('diagnosticos/', views.diagnostico_list, name='diagnostico-list'),
    path('diagnosticos/<int:pk>/', views.diagnostico_detail, name='diagnostico-detail'),
]