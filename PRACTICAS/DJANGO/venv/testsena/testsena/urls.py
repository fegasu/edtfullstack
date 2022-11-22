"""testsena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from ppal import views
from proyectos import views as proy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('0', views.index),
    path('1/0', proy.indexP),
    path('1/1', proy.newP),
    path('1/2/<mid>', proy.EditP),
    path('salvaproy/', proy.salvaproy),
    path('newproy/', proy.InsertarProy),
    path('delproy/<pid>', proy.borrarproy),

]
