import os
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from django.template import Template,Context
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def index(request):
    #BASE_DIR=BASE_DIR+"testsena/ppal/plantillas/index.html"
    #doc=open("C:/Users/User1/Desktop/DJANGO/venv/testsena/ppal/plantillas/index.html")
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    doc=open(os.path.join(os.path.dirname(BASE_DIR),"testsena\\ppal\\plantillas/index.html"))
    plt=Template(doc.read())
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

