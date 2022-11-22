import os
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from django.template import Template,Context
from django import forms
from ppal.models import PROYECTOS
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def indexP(request):
    todo=PROYECTOS.objects.all()
    #BASE_DIR=BASE_DIR+"testsena/ppal/plantillas/index.html"
    #doc=open("C:/Users/User1/Desktop/DJANGO/venv/testsena/ppal/plantillas/index.html")
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    doc=open("C:/Users/User1/Desktop/DJANGO/venv/testsena/proyectos/plantillas/index.html")
    plt=Template(doc.read())
    ctx=Context({"lista":todo})
    documento=plt.render(ctx)
    return HttpResponse(documento)
def newP(request):
    #BASE_DIR=BASE_DIR+"testsena/ppal/plantillas/index.html"
    #doc=open("C:/Users/User1/Desktop/DJANGO/venv/testsena/ppal/plantillas/index.html")
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    doc=open("C:/Users/User1/Desktop/DJANGO/venv/testsena/proyectos/plantillas/proynuevo.html")
    plt=Template(doc.read())
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)
def EditP(request,mid):
    record = PROYECTOS.objects.get(id = mid)
    #BASE_DIR=BASE_DIR+"testsena/ppal/plantillas/index.html"
    #doc=open("C:/Users/User1/Desktop/DJANGO/venv/testsena/ppal/plantillas/index.html")
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    doc=open("C:/Users/User1/Desktop/DJANGO/venv/testsena/proyectos/plantillas/EditaProy.html")
    plt=Template(doc.read())
    ctx=Context({"lista":record})
    documento=plt.render(ctx)
    return HttpResponse(documento)
def salvaproy(request):
    a="""<center><h2>PROYECTO ACTUALIZADO</h2>
    <script>
    function Ir(){
    location.href="/1/0";
    }
    setTimeout('Ir()',2000);
        </script>
    """
    
    vid=request.GET["V"]
    nombre=request.GET["nombre"]
    prefi=request.GET["prefi"]
    descri=request.GET["descri"]
    
    p=PROYECTOS.objects.get(id=vid)
    p.nom=nombre;p.descripcion=descri;p.prefijo=prefi
    p.save()
    return HttpResponse(a)

def InsertarProy(request):
    a="""<center><h2>PROYECTO CREADO SATISFACTORIAMENTE...</h2>
    <script>
    function Ir(){
    location.href="/1/0";
    }
    setTimeout('Ir()',2000);
        </script>
    """
    nombre=request.GET["nombre"]
    vprefi=request.GET["prefi"]
    descri=request.GET["descri"]
    vactivo=request.GET["dispo"]
    pro=PROYECTOS(nom=nombre,descripcion=descri,activo=vactivo,prefijo=vprefi)
    pro.save()
    return HttpResponse(a)
def borrarproy(request,pid):
    a="""<center><h2>PROYECTO BORRADO SATISFACTORIAMENTE...</h2>
    <script>
    function Ir(){
    location.href="/1/0";
    }
    setTimeout('Ir()',2000);
        </script>
    """
    p=PROYECTOS.objects.get(id=pid)
    p.delete()
    return HttpResponse(a)
    
    
               
    
    