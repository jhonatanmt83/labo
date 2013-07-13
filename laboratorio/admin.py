#encoding:utf-8
from django.contrib import admin
from laboratorio.models import Laboratorio, Encargado

admin.site.register(Laboratorio)
admin.site.register(Encargado)