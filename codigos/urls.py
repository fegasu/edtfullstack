from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from academico.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('coor/<N>/<R>', coor),
]
