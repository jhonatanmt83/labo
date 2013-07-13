#encoding:utf-8
from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    name = models.CharField(
        max_length = 10,
        help_text = "Nombre de laboratorio",
        verbose_name = "Nombre")
    state_choices = ((0, 'libre'),
        (1, 'en mantemiento'),
        (2, 'no disponible'),
        (3, 'en clase'))
    state = models.CharField(
        max_length = 1,
        help_text = "estado de laboratorio",
        verbose_name = "estado",
        choices = state_choices)


class Encargado(models.Model):
    fullname = models.CharField(
        max_length = 255,
        help_text = "nombre completo del encargado",
        verbose_name = "nombre")
    laboratorio = models.ManyToManyField(Laboratorio)