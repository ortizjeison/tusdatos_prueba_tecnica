
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from apis import consultar_causas 
# setting path

def test_contar_causas_demandado():
    consultar_causas.consultar_causas_demandado(105,"1791251237001")

def test_consultar_causas_demandante():
    consultar_causas.consultar_causas_demandante(157,"0968599020001")