from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



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
    path("buscar" , views.buscar),
    
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    
    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),
    path("editar_profesor/<int:id>" , views.editar_profesor, name="editar_profesor"),
    
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="Register"),
    
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")
    
]
