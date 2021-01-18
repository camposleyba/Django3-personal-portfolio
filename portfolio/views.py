from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    projects = Project.objects.all() # con esta sentencia traigo todos los obejtos de la base de datas a la pagina home
    return render(request, 'portfolio/home.html', {'projects':projects}) #acá paso dichos objetos como un diccionario
