from django import forms
import datetime

class PostForm(forms.Form):

    #usuario = forms.CharField()
    titulo = forms.CharField()
    descripcion = forms.CharField()
    #imagen = forms.ImageField(upload_to='img_post', blank=True, null=True)
    #date = forms.DateField()

class NovedadForm(forms.Form):
    #usuario = forms.CharField()
    titulo = forms.CharField()
    descripcion = forms.CharField()
    #imagen = forms.ImageField(upload_to='img_post', blank=True, null=True)
    #date = forms.DateField()