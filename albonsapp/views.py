from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Post
from .forms import PostForm
import datetime
#from albonsapp.forms import CustomUserCreationForm

def index(req):

    return render(req, 'index.html')

#login
def login_view(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "index.html", {"message": f"hola {usuario}"})
            else:

                return render(req, "index.html", {"message": "datos erroneos"})
    
    else:
        miFormulario = AuthenticationForm

        return render(req, "login.html", {"miFormulario": miFormulario})
    

#registro usuario
def registro(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            miFormulario.save()

            return render(req, "index.html", {"message": f"Usuario {usuario} creado con éxito"})
        
        else:

            return render(req, "index.html", {"message": "Datos invalidos"})
    
    else:
        miFormulario = UserCreationForm()

        return render(req, "registro.html", {"miFormulario": miFormulario})
    

#ver los Posteos
def posts(req):

    lista = Post.objects.all()

    return render(req, 'posts.html', {"lista_posts":lista})


#formulario Post
def postForm(req):
    
    
    usuarioLog = req.user.username

    if req.method == 'POST':

        miFormulario = PostForm(req.POST)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            fecha = datetime.datetime.now()

            nuevo_post = Post(usuario=usuarioLog, titulo=data['titulo'], descripcion=data['descripcion'], date=fecha)
            nuevo_post.save()
            
            return render(req, 'index.html', {"message": "Post creado con éxito"})
        else:
            return render(req, 'index.html', {"message": "Datos no validos"})
    else:

        miFormulario = PostForm()

        return render(req, 'post_formulario.html', {"miFormulario": miFormulario})
    