#API imports

from apis import consultar_causas
from apis import contar_causas
from apis import datos_generales
from apis import datos_generales
from apis import info_juicio
from apis import actuaciones_judiciales

from pysondb import db
from datetime import datetime

def query_demandado(documento):
    response = {}
    
    try:
        num_causas = contar_causas.contar_causas_demandado(documento)
    except Exception as e:
            print(f'Error when calling contar_causas_demandado: {e}')
    try:
        causas = consultar_causas.consultar_causas_demandado(num_causas,documento)
    except Exception as e:
            print(f'Error when calling consultar_causas_demandado: {e}')

    #Query info_juicio for each element (juicio)

    for juicio in causas:
        
        id_juicio = juicio.get('idJuicio')

        try:
            datos_juicio = info_juicio.get_info_juicio(id_juicio)
        except Exception as e:
            print(f'Error when calling get_info_juicio: {e} ({id_juicio})')
        
        try:            
            datos_generales_juicio = datos_generales.get_datos_generales(id_juicio)
        except Exception as e:
            print(f'Error when calling get_datos_generales: {e} ({id_juicio})')

        #Get data from datos_generales to query actuaciones_judiciales
        idMovimientoJuicioIncidente = datos_generales_juicio[0].get('lstIncidenteJudicatura')[0].get('idMovimientoJuicioIncidente')
        idJudicatura = datos_generales_juicio[0].get('idJudicatura')
        idIncidenteJudicatura = datos_generales_juicio[0].get('lstIncidenteJudicatura')[0].get('idIncidenteJudicatura')
        nombreJudicatura = idJudicatura = datos_generales_juicio[0].get('nombreJudicatura')

        try:
            actuaciones_datos = actuaciones_judiciales.get_actuaciones_judiciales(idMovimientoJuicioIncidente,id_juicio,idJudicatura,idIncidenteJudicatura,nombreJudicatura)
        except Exception as e:
            print(f'Error when calling get_actuaciones_judiciales: {e} ({idMovimientoJuicioIncidente,id_juicio,idJudicatura,idIncidenteJudicatura,nombreJudicatura})')
            actuaciones_datos = {}


        juicio['info_juicio'] = datos_juicio
        juicio['datos_generales'] = datos_generales_juicio
        juicio['actuaciones_judiciales'] = actuaciones_datos

    response['tipo_consulta'] = 'Demandado'
    response['documento'] = documento
    response['fecha_de_consulta'] = str(datetime.now())
    response['causas'] = causas

    database = db.getDb('database.json')
    id = database.add(response)
    return response


def query_demandante(documento):
    response = {}
    
    
    try:
        num_causas = contar_causas.contar_causas_demandante(documento)
    except Exception as e:
        print(f'Error when calling contar_causas_demandante: {e}')
    try:
        causas = consultar_causas.consultar_causas_demandante(num_causas,documento)
    except Exception as e:
        print(f'Error when calling consultar_causas_demandante: {e}')

    #Query info_juicio for each element (juicio)

    for juicio in causas:
        
        id_juicio = juicio.get('idJuicio')

        try:
            datos_juicio = info_juicio.get_info_juicio(id_juicio)
        except Exception as e:
            print(f'Error when calling get_info_juicio: {e}')
        
        try:
            
            datos_generales_juicio = datos_generales.get_datos_generales(id_juicio)
        except Exception as e:
            print(f'Error when calling get_datos_generales: {e}')

        #Get data from datos_generales to query actuaciones_judiciales
        idMovimientoJuicioIncidente = datos_generales_juicio[0].get('lstIncidenteJudicatura')[0].get('idMovimientoJuicioIncidente')
        idJudicatura = datos_generales_juicio[0].get('idJudicatura')
        idIncidenteJudicatura = datos_generales_juicio[0].get('lstIncidenteJudicatura')[0].get('idIncidenteJudicatura')
        nombreJudicatura = idJudicatura = datos_generales_juicio[0].get('nombreJudicatura')

        try:
            actuaciones_datos = actuaciones_judiciales.get_actuaciones_judiciales(idMovimientoJuicioIncidente,id_juicio,idJudicatura,idIncidenteJudicatura,nombreJudicatura)
        except Exception as e:
            print(f'Error when calling get_actuaciones_judiciales: {e}')
            actuaciones_datos = {}

        juicio['info_juicio'] = datos_juicio
        juicio['datos_generales'] = datos_generales_juicio
        juicio['actuaciones_judiciales'] = actuaciones_datos

    response['tipo_consulta'] = 'Demandante'
    response['documento'] = documento
    response['fecha_de_consulta'] = str(datetime.now())
    response['causas'] = causas

    database = db.getDb('database.json')
    database.add(response)
    return response

if __name__ == "__main__":
    print(query_demandado('1791251237001'))