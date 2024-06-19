from django import forms
import datetime

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model=User
        fields=["first_name", "last_name"]