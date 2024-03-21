
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from apis import datos_generales
# setting path

def tests_datos_generales():
    datos_generales.get_datos_generales("13284202406765")