from apis import custom_requests

def get_datos_generales(idJuicio):
    
    url = f"https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-CLEX-SERVICE/api/consulta-causas-clex/informacion/getIncidenteJudicatura/{idJuicio}"

    payload = {}
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

    response = custom_requests.request("GET", url, headers,payload)

    return response.json()