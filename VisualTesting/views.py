# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import subprocess

from django.shortcuts import render

from django.views import View


# Create your views here.
from django.urls import reverse

from CmdAJAR import ejecutar_comando


class IndexView(View):
    def get(self, request):
        # res = subprocess.call(["node", "C:/AJAR/Pruebas Auto/PA-Taller6/AppNode/appResemble.js"])
        res_resemble = None
        error_general = None
        res_cypress = None
        try:
            res_cypress = ejecutar_comando(["./node_modules/cypress/bin/cypress", "run", "."])

            res_resemble = ejecutar_comando(["node", "./AppNode/appResemble.js"])
        except Exception, error:
            error_general = "Ocurrió un error durante la ejecución de la prueba: " + error.__str__()

        return render(request, 'Index.html', {'res_cypress': res_cypress,
                                              'res_resemble': res_resemble,
                                              'error_general': error_general})
