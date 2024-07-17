from django.urls import path
from app_cadastro_users import views

urlpatterns = [
    path("", views.home, name="home"),
    path("usuarios/", views.usuarios, name="lista_users"),
]
