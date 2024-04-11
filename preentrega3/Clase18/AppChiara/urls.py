from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio , name="Home"),
    path("ver_cursos", views.ver_cursos , name="Cursos"),
    path("ver_alumnos", views.ver_alumnos , name="Ver alumnos"),
    path("ver_profesores", views.ver_profesores , name="Ver profesores"),
    #path("alta_curso/<nombre>", views.alta_curso),
    
    path("alta_curso", views.curso_formulario, name="Agregar Curso"),
    path("alta_alumno", views.alumno_formulario, name="Agregar Alumno"),
    path("alta_profe", views.profesor_formulario, name="Agregar Profesor"),
    
    
    path("buscar_curso" , views.buscar_curso, name="Buscar Curso"),
    path("buscar" , views.buscar)
    
    
    ]
