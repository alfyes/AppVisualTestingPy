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
        #res = subprocess.call(["node", "C:/AJAR/Pruebas Auto/PA-Taller6/AppNode/appResemble.js"])
        ejecutar_comando()

        return render(request, 'Index.html', ejecutar_comando())
