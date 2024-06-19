from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, login_view, registro, posts, postForm, novedadForm, novedades, elimina_post, elimina_novedad, editar_perfil


urlpatterns = [
    path('index/', index, name="index"),
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(template_name="index.html"), name="logout"),
    path('registro/', registro, name="registro"),
    path('posts/', posts, name="posts"),
    path('post_formulario/', postForm, name="postForm"),
    path('novedad_formulario/', novedadForm, name="novedadForm"),
    path('novedades/', novedades, name="novedades"),
    path('elimina_post/<int:id>', elimina_post, name='eliminaPost'),
    path('eliminar_novedad/<int:id>', elimina_novedad, name='eliminaNovedad'),
    path('editar_perfil/', editar_perfil, name='editarPerfil')
]
