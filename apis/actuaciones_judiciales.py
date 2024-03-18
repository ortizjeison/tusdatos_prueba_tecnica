from .custom_requests import request
import json
from pysondb import db
from datetime import datetime

def get_actuaciones_judiciales(idMovimientoJuicioIncidente,idJuicio,idJudicatura,idIncidenteJudicatura,nombreJudicatura):


    url = "https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/actuacionesJudiciales"

    payload = json.dumps({
    "idMovimientoJuicioIncidente": idMovimientoJuicioIncidente,
    "idJuicio": idJuicio,
    "idJudicatura": idJudicatura,
    "idIncidenteJudicatura": idIncidenteJudicatura,
    "aplicativo": "web",
    "nombreJudicatura": nombreJudicatura,
    "incidente": 1
    })
    
    headers = {
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'host': 'api.funcionjudicial.gob.ec'
    }


    try:
        response = request("POST", url, headers,payload)
        resp = response.json()
    except Exception as e:
        error_log = {'timestamp':str(datetime.now()),'idJuicio': idJuicio, "Server_response": response.text, "exception": str(e)}
        print(error_log)
        database = db.getDb('errors.json')
        database.add(error_log)


    actuaciones_cleaned = []

    for actuacion in resp:
        actuacion = {
            "codigo": actuacion.get('codigo'),
            "idJudicatura": actuacion.get('idJudicatura'),
            "idJuicio": actuacion.get('idJuicio'),
            "fecha": actuacion.get('fecha'),
            "tipo": actuacion.get('tipo'),
            "actividad": actuacion.get('actividad')
            }
        
        actuaciones_cleaned.append(actuacion)


    return actuaciones_cleaned

if __name__ == "__main__":
    actuaciones_judiciales = get_actuaciones_judiciales("26010324", '09332202403102', 'UNIDAD JUDICIAL CIVIL CON SEDE EN EL CANTÓN GUAYAQUIL', "27384010", 'UNIDAD JUDICIAL CIVIL CON SEDE EN EL CANTÓN GUAYAQUIL')
    print(actuaciones_judiciales)