import requests
import json
from pysondb import db
from datetime import datetime

def get_actuaciones_judiciales(idMovimientoJuicioIncidente,idJuicio,idJudicatura,idIncidenteJudicatura,nombreJudicatura):

    proxies = {
   'http': 'http://186.215.87.194:6010',
   'http': 'http://186.103.130.93:8080'
    }

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
    'host': 'api.funcionjudicial.gob.ec',
    'Cookie': 'CJ=2853568778.31775.0000'
    }

    response = requests.request("POST", url, headers=headers, data=payload, timeout=60,proxies=proxies)
    
    try:
        resp = response.json()
    except:
        error_log = {'Timestamp':str(datetime.now()),'idJuicio': idJuicio, "Error": response.text}
        print(error_log)
        database = db.getDb('errors.json')
        database.add(error_log)

    return resp 

if __name__ == "__main__":
    actuaciones_judiciales = get_actuaciones_judiciales("25989939","13284202406765","13284","27362897","UNIDAD JUDICIAL PENAL DE MANTA")
    print(actuaciones_judiciales)