# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import subprocess

from datetime import datetime
from django.shortcuts import render, redirect

from django.views import View

import shutil
import time
# Create your views here.
from django.urls import reverse

from CmdAJAR import ejecutar_comando
from VisualTesting.models import Reporte


class IndexView(View):
    def get(self, request):
        reportes = Reporte.objects.all().order_by('-fecha')
        return render(request, 'Index.html', {'reportes': reportes})

    def post(self, request):
        # res = subprocess.call(["node", "C:/AJAR/Pruebas Auto/PA-Taller6/AppNode/appResemble.js"])
        res_resemble = None
        error_general = None
        res_cypress = None
        try:
            marca_tiempo = long(time.time() * 10)
            ruta_imagen_1 = './TestImages/primera_{0}.png'.format(marca_tiempo)
            ruta_imagen_2 = './TestImages/segunda_{0}.png'.format(marca_tiempo)
            ruta_imagen_salida = './TestImages/salida_{0}.png'.format(marca_tiempo)

            res_cypress = ejecutar_comando(["./node_modules/cypress/bin/cypress", "run"])

            shutil.copyfile('./cypress/screenshots/primerpantallazo.png',
                            ruta_imagen_1)
            shutil.copyfile('./cypress/screenshots/segundopantallazo.png',
                            ruta_imagen_2)

            res_resemble = ejecutar_comando(["node", "./AppNode/appResemble.js"])

            shutil.copyfile('./AppNode/salidas/resultado.png',
                            ruta_imagen_salida)

            reporte = Reporte(imagen_1=ruta_imagen_1[1:],
                              imagen_2=ruta_imagen_2[1:],
                              imagen_salida=ruta_imagen_salida[1:],
                              fecha=datetime.today(),
                              info_comparacion=res_resemble['salida'])
            reporte.save()

        except Exception, error:
            error_general = "Ocurrio un error durante la ejecucion de la prueba: " + error.__str__()
            print error_general

        return redirect(reverse('visual_testing:index'))
