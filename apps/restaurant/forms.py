from django import forms

class UserForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    correo = forms.EmailField()
    password = forms.CharField(max_length=255)