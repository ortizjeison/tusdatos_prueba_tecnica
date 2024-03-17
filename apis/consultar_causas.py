from .custom_requests import request
import json


def consultar_causas_demandado(num_causas,documento):
    url = f"https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/buscarCausas?size={num_causas}"

    payload = json.dumps({
    "numeroCausa": "",
    "actor": {
        "cedulaActor": "",
        "nombreActor": ""
    },
    "demandado": {
        "cedulaDemandado": documento,
        "nombreDemandado": ""
    },
    "provincia": "",
    "numeroFiscalia": "",
    "recaptcha": "verdad"
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
    'Cookie': 'CJ=2870345994.31775.0000'
    }

    response = request("POST", url, headers,payload)

    cleaned_response = []

    for causa in response.json():
        causa_cleaned = {
            "id": causa.get('id'),
            "idJuicio": causa.get('idJuicio'),
            "estadoActual": causa.get('estadoActual'),
            "idMateria": causa.get('idMateria'),
            "nombreDelito": causa.get('nombreDelito'),
            "fechaIngreso": causa.get('fechaIngreso')
            }
        
        cleaned_response.append(causa_cleaned)
    
    return cleaned_response 


def consultar_causas_demandante(num_causas,documento):
    url = f"https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/buscarCausas?size={num_causas}"

    payload = json.dumps({
    "numeroCausa": "",
    "actor": {
        "cedulaActor": documento,
        "nombreActor": ""
    },
    "demandado": {
        "cedulaDemandado": "",
        "nombreDemandado": ""
    },
    "provincia": "",
    "numeroFiscalia": "",
    "recaptcha": "verdad"
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

    response =request("POST", url, headers, payload)

    cleaned_response = []

    for causa in response.json():
        causa_cleaned = {
            "id": causa.get('id'),
            "idJuicio": causa.get('idJuicio'),
            "estadoActual": causa.get('estadoActual'),
            "idMateria": causa.get('idMateria'),
            "nombreDelito": causa.get('nombreDelito'),
            "fechaIngreso": causa.get('fechaIngreso')
            }
        
        cleaned_response.append(causa_cleaned)
    print("Consultar_causas Done")
    return cleaned_response 


if __name__ == "__main__":
    causas_demandado = consultar_causas_demandado(105,'1791251237001')
    #print(causas_demandado)

    causas_demandante = consultar_causas_demandante(157,'0968599020001')
    #print(causas_demandado)