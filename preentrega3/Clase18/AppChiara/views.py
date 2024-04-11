from django.shortcuts import render
from AppChiara.models import Curso
from django.http import HttpResponse 
from django.template import loader
from AppChiara.forms import Curso_formulario
from AppChiara.forms import Alumno_formulario
from AppChiara.forms import Profesor_formulario
from AppChiara.models import Alumno
from AppChiara.models import Profesor

# Create your views here.

def inicio(request):
    return render(request, "padre.html")

# def alta_curso(request,nombre):
#     curso = Curso(nombre=nombre, camada=230805)
#     curso.save()
#     texto = f"Se guardo en la base de datos el curso: {curso.nombre} {curso.camada}"
#     return HttpResponse(texto)


# def alta_alumnos(request,nombre):
#     alumno = Alumno(nombre=nombre, edad=18)
#     alumno.save()
#     texto = f"El/la alumno/a quedo guardado/a en la base de datos: {alumno.nombre} {alumno.edad}"
#     return HttpResponse(texto)


# def alta_profesores(request,nombre,apellido):
#     profesor = Profesor(nombre=nombre, apellido=apellido)
#     profesor.save()
#     texto = f"El/la profesor/a quedo guardado/a en la base de datos: {profesor.nombre} {profesor.apellido}"
#     return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)




def alumno_formulario(request):
    
    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
        
            datos = mi_formulario.cleaned_data
        
            alumno =Alumno( nombre=datos["nombre"] , edad=datos["edad"])
            alumno.save()
            return render(request , "alta_alumno.html")
    
    return render(request , "alta_alumno.html")


def profesor_formulario(request):
    
    if request.method == "POST":
        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
        
            datos = mi_formulario.cleaned_data

            profesor =Profesor( nombre=datos["nombre"] , apellido=datos["apellido"])
            profesor.save()
            
            return render(request , "alta_profe.html")
    
    return render(request , "alta_profe.html")


def curso_formulario(request):
    
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
        
         datos = mi_formulario.cleaned_data
        
         curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
         curso.save()
         return render(request , "formulario.html")
    
    return render(request , "formulario.html")



def buscar_curso(request):
    return render(request , "buscar_curso.html")



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")