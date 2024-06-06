from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from .models import Usuario
from django.http import HttpResponse
import time
# Create your views here.

def get_user_info(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nombre']
            email = form.cleaned_data['correo']
            passw = form.cleaned_data['password']
            user = Usuario.objects.create(
                nombre=name,
                correo=email,
                password=passw)
            user.save()
            
            messages .success(request,'Usuario fue creado con exito.')
            time.sleep(3)
            return  redirect('/rest/user')
    if  request.method == 'GET':
        form = UserForm()
    
    return render(request,'index.html',{'form':form})
        