import requests
import json


def contar_causas_demandado(documento):
    url = "https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/contarCausas"

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
    'host': 'api.funcionjudicial.gob.ec'
    }

    response = requests.request("POST", url, headers=headers, data=payload, timeout=60)
    return response.text


def contar_causas_demandante(documento):
    url = "https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/contarCausas"

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

    response = requests.request("POST", url, headers=headers, data=payload, timeout=60)
    return response.text


if __name__ == "__main__":
    num_causas_demandante = contar_causas_demandante("0968599020001")
    print(num_causas_demandante)

    num_causas_demandado = contar_causas_demandado("1791251237001")
    print(num_causas_demandado)