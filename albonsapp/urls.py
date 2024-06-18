from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, login_view, registro, posts, postForm


urlpatterns = [
    path('index/', index, name="index"),
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(template_name="index.html"), name="logout"),
    path('registro/', registro, name="registro"),
    path('posts/', posts, name="posts"),
    path('post_formulario/', postForm, name="postForm"),
]
