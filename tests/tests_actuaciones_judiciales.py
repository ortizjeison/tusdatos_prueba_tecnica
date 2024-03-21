import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from apis import actuaciones_judiciales
# setting path

def test_info_juicio():
    actuaciones_judiciales.get_actuaciones_judiciales("26010324", '09332202403102', 'UNIDAD JUDICIAL CIVIL CON SEDE EN EL CANTÓN GUAYAQUIL', "27384010", 'UNIDAD JUDICIAL CIVIL CON SEDE EN EL CANTÓN GUAYAQUIL')