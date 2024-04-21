from django.shortcuts import render
from AppChiara.models import Curso
from django.http import HttpResponse 
from django.template import loader
from AppChiara.forms import Curso_formulario
from AppChiara.forms import Alumno_formulario
from AppChiara.forms import Profesor_formulario
from AppChiara.models import Alumno
from AppChiara.models import Profesor, Avatar
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from AppChiara.forms import UserEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request, "padre.html", {"url": avatares[0].imagen.url if avatares.exists() else None})

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
    avatares = Avatar.objects.filter(user=request.user.id)
    

    return render( request , "cursos.html", {"cursos":cursos, "url": avatares[0].imagen.url if avatares.exists() else None})



def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)

    return render( request , "alumnos.html", {"alumnos":alumnos, "url": avatares[0].imagen.url if avatares.exists() else None})



def ver_profesores(request):
    profesores = Profesor.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render( request , "profesores.html", {"profesores":profesores, "url": avatares[0].imagen.url if avatares.exists() else None})




def alumno_formulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
        
            datos = mi_formulario.cleaned_data
            alumno =Alumno( nombre=datos["nombre"] , edad=datos["edad"])
            alumno.save()
            return render(request , "alta_alumno.html", {"url": avatares[0].imagen.url if avatares.exists() else None})
    
    return render(request , "alta_alumno.html", {"url": avatares[0].imagen.url if avatares.exists() else None})


def profesor_formulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if request.method == "POST":
        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
        
            datos = mi_formulario.cleaned_data

            profesor =Profesor( nombre=datos["nombre"] , apellido=datos["apellido"])
            profesor.save()
            
            return render(request , "alta_profe.html", {"url": avatares[0].imagen.url if avatares.exists() else None})
    
    return render(request , "alta_profe.html", {"url": avatares[0].imagen.url if avatares.exists() else None})


def curso_formulario(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if request.method == "POST":
        
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
        
         datos = mi_formulario.cleaned_data
        
         curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
         curso.save()
         return render(request , "formulario.html", {"url": avatares[0].imagen.url if avatares.exists() else None})
    
    return render(request , "formulario.html", {"url": avatares[0].imagen.url if avatares.exists() else None})


def buscar_curso(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "buscar_curso.html",  {"url": avatares[0].imagen.url if avatares.exists() else None})



def buscar(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos, "url": avatares[0].imagen.url if avatares.exists() else None})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
    
    
def elimina_curso(request , id):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso, "url": avatares[0].imagen.url if avatares.exists() else None})


def elimina_alumno(request , id ):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    
    alumno = Alumno.objects.all()
    
    return render(request , "alumnos.html" , {"alumnos":alumno, "url": avatares[0].imagen.url if avatares.exists() else None})


def elimina_profesor(request , id ):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    
    profesor = Profesor.objects.all()
    
    return render(request , "profesores.html" , {"profesores":profesor, "url": avatares[0].imagen.url if avatares.exists() else None})





def editar(request , id):
    avatares = Avatar.objects.filter(user=request.user.id)

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso, "url": avatares[0].imagen.url if avatares.exists() else None})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso, "url": avatares[0].imagen.url if avatares.exists() else None})




def editar_alumno(request , id):
    avatares = Avatar.objects.filter(user=request.user.id)

    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.edad = datos["edad"]
            alumno.save()

            alumno = Alumno.objects.all()

            return render(request , "alumnos.html" , {"alumnos":alumno, "url": avatares[0].imagen.url if avatares.exists() else None})


        
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre , "edad":alumno.edad})
    
    return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno, "url": avatares[0].imagen.url if avatares.exists() else None})



def editar_profesor(request , id):
    avatares = Avatar.objects.filter(user=request.user.id)

    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.apellido = datos["apellido"]
            profesor.save()

            profesor = Profesor.objects.all()

            return render(request , "profesores.html" , {"profesores":profesor, "url": avatares[0].imagen.url if avatares.exists() else None})


        
    else:
        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre , "apellido":profesor.apellido})
    
    return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor, "url": avatares[0].imagen.url if avatares.exists() else None})




def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url, "mensaje":f"Bienvenido/a {usuario}", "usuario":usuario})
            else:
                return HttpResponse("Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})




def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})


def editarPerfil(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario, "url": avatares[0].imagen.url if avatares.exists() else None})
