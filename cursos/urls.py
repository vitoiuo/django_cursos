from django.urls import path
from . import views
import cursos

urlpatterns = [
    path("", views.pagina_inicial, name='cursos_inicio'),
    path("listar/meus_cursos/", views.listar_cursos, name='meus_cursos'),
]