from django.db import models
import datetime

class PostModel(models.Model):

    usuario = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imgPost', blank=True, null=True)

class Post(models.Model):

    usuario = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imgPost', blank=True, null=True)
    date = models.DateField(datetime.date.today)


class Novedad(models.Model):

    usuario = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imgPost', blank=True, null=True)
    date = models.DateField(datetime.date.today)