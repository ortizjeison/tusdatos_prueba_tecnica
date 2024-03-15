#API imports
from .consultar_causas import *
from .contar_causas import *
from .datos_generales import *
from .datos_generales import *
from .info_juicio import *
from .actuaciones_judiciales import *

from pysondb import db

def query_demandado(documento):
    
    num_causas = contar_causas_demandado(documento)
    causas = consultar_causas_demandado(num_causas,documento)

    #Query info_juicio for each element (juicio)

    for juicio in causas:
        
        id_juicio = juicio.get('idJuicio')

        info_juicio = get_info_juicio(id_juicio)
        datos_generales = get_datos_generales(id_juicio)

        #Get data from datos_generales to query actuaciones_judiciales
        idMovimientoJuicioIncidente = datos_generales[0].get('lstIncidenteJudicatura')[0].get('idMovimientoJuicioIncidente')
        idJudicatura = datos_generales[0].get('idJudicatura')
        idIncidenteJudicatura = datos_generales[0].get('lstIncidenteJudicatura')[0].get('idIncidenteJudicatura')
        nombreJudicatura = idJudicatura = datos_generales[0].get('nombreJudicatura')

        try:
            actuaciones_judiciales = get_actuaciones_judiciales(idMovimientoJuicioIncidente,id_juicio,idJudicatura,idIncidenteJudicatura,nombreJudicatura)
        except:
            actuaciones_judiciales = {}

        juicio['info_juicio'] = info_juicio
        juicio['datos_generales'] = datos_generales
        juicio['actuaciones_judiciales'] = actuaciones_judiciales

    return causas

#@Todo: query_demandante


if __name__ == "__main__":
    print(query_demandado('1791251237001'))