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

    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["first_name", "last_name"]

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2