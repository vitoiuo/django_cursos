from django.urls import path
from . import views
import cursos

urlpatterns = [
    path("", views.pagina_inicial)
]