import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from AA_Funciones_Globales_Total.Funciones_Globales_Total import Funciones_Globales_Total #para llamar las funciones viene de la carpeta y funcion
import random
import pytest
import sys #Libreria para informacion directamente del sistema operativo

#playwright codegen https://www.saucedemo.com/
tiempo=0.3
ruta="Imagenes_Globales/Select"
pdf1="C:/Practica_Playwright/18_Unpload_Files/Imagenes/Upload/Playwright_Prueba_Upload.jpg"
#invertir la diagonal, \ por /

#@pytest.mark.parametrize("Numero,Esperando", [("3+5", 8), ("2+4", 6),("6*9", 42),("9*5",45)])
@pytest.mark.parametrize("Numero,Esperando", [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail),("9*5",45)])
def test_eval(Numero, Esperando):
    assert eval(Numero) == Esperando