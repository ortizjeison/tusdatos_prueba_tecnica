import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from apis import contar_causas 
# setting path

def test_contar_causas_demandado():
    contar_causas.contar_causas_demandado("1791251237001")

def test_contar_causas_demandante():
    contar_causas.contar_causas_demandante("0968599020001")