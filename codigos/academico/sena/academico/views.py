import os
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from django.template import Template,Context
from django.template import loader
from .models import *

# Create your views here.
def index(request):
    documento="""<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"><div class="container" style='width:60%;margin:auto;'>
   <center><img src="/static/imgs/BLOG.png" class="w3-panel w3-round-xxlarge" style="border:true;width:90%;border-color:black;height:150px;-webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
-moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);border: 1px solid #000000;"><h2><b>EDT FULLSTACK DEVELOPER WITH PYTHON-DJANGO V1.0<b></h2><button class='w3-blue w3-round-xxlarge ' style='width:200px;' onclick=javascript:location.href='/coor/0/0'>&nbsp;&nbsp;&nbsp;Iniciar&nbsp;&nbsp;</button>"""
    return HttpResponse(documento)
    
def coor(request,N,R):
    documento=""
    if N == '0':
        todo=COORDINACION.objects.all()
        plt=loader.get_template('coordinacion.html')
        documento=plt.render({"lista":todo,"N":N})        
    if N == '1':
        plt=loader.get_template('coordinacion.html')
        documento=plt.render({"N":N})    
    if N == '11':
        nombre=request.GET["nombre"]
        coordina=COORDINACION(nom=nombre)
        coordina.save()
        documento="""<div class="container" style='width:40%;margin:auto;'>
   <center><img src="/static/imgs/BLOG.png" class="w3-panel w3-round-xxlarge" style="border:true;width:90%;border-color:black;height:150px;-webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
-moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);border: 1px solid #000000;"><h2>COORDINACION CREADA SATISFACTORIAMENTE...</h2>
    <script>
    function Ir(){
    location.href="/coor/0/0";
    }
    setTimeout('Ir()',2000);
        </script>
        """         
    if N == '2':
        p=COORDINACION.objects.get(id=R)
        plt=loader.get_template('coordinacion.html')
        documento=plt.render({"lista":p,"N":N})   
    if N == '21':   
        p=COORDINACION.objects.get(id=R)
        nombre=request.GET["nombre"]
        p.nom=nombre
        p.save()
        documento="""<div class="container" style='width:40%;margin:auto;'>
   <center><img src="/static/imgs/BLOG.png" class="w3-panel w3-round-xxlarge" style="border:true;width:90%;border-color:black;height:150px;-webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
-moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);border: 1px solid #000000;"><h2>COORDINACION GUARDADA SATISFACTORIAMENTE...</h2>
    <script>
    function Ir(){
    location.href="/coor/0/0";
    }
    setTimeout('Ir()',2000);
        </script>
        """  
    if N == '3':
        p=COORDINACION.objects.get(id=R)
        plt=loader.get_template('coordinacion.html')
        documento=plt.render({"lista":R,"N":N}) 
    if N == '31':
        p=COORDINACION.objects.get(id=R)
        p.delete()
        documento="""<div class="container" style='width:40%;margin:auto;'>
   <center><img src="/static/imgs/BLOG.png" class="w3-panel w3-round-xxlarge" style="border:true;width:90%;border-color:black;height:150px;-webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
-moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);border: 1px solid #000000;"><h2>COORDINACION BORRADA SATISFACTORIAMENTE...</h2>
    <script>
    function Ir(){
    location.href="/coor/0/0";
    }
    setTimeout('Ir()',2000);
        </script>
        """
               
    return HttpResponse(documento)
    