# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Reporte(models.Model):
    fecha = models.DateTimeField(verbose_name='Fecha', null=False, blank=False)
    imagen_1 = models.TextField(max_length=100, verbose_name='Imagen 1', null=False, blank=False)
    imagen_2 = models.TextField(max_length=100, verbose_name='Imagen 2', null=False, blank=False, unique=True)
    imagen_salida = models.TextField(max_length=100, verbose_name='Imagen Salida', null=False, blank=False)
    info_comparacion = models.TextField(max_length=5, verbose_name='Información de la comparación', null=False, blank=False)

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

