from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Hola desde django")

def miEdad(reques, edad):
    return HttpResponse("Hola tu edad es: %s" %edad)