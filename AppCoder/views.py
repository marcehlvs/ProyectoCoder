from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso


# Create your views here.

def curso(request):

    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoTexto)
