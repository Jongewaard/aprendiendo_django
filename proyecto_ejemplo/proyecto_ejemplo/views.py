
from django.http import HttpResponse
from django.template import Template, Context

def hello(request):
    return HttpResponse("Hola gato")

def hello_name(request, nombre, apellido):
    return HttpResponse(f"Hola {nombre} {apellido}")

def inicio(request):

    mi_template = open("C:/Users/gjdba/Documents/Trading Bot/Trading BOT v2/Django/proyecto_ejemplo/proyecto_ejemplo/templates/index.html","r")

    plantilla = Template(mi_template.read())

    mi_template.close()

    contexto = Context()

    documento_a_devolver = plantilla.render(contexto)

    return HttpResponse(documento_a_devolver)

