from apis import custom_requests


def get_info_juicio(idJuicio):

    url = f"https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/getInformacionJuicio/{idJuicio}"

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
      'host': 'api.funcionjudicial.gob.ec'
    }

    
    response = custom_requests.request("GET", url,headers,payload)
    

    juicio_cleaned = []

    for juicio in response.json():
        juicio = {
            "idJuicio": juicio.get('idJuicio'),
            "nombreDelito": juicio.get('nombreDelito'),
            "fechaIngreso": juicio.get('fechaIngreso'),
            "nombreMateria": juicio.get('nombreMateria'),
            "nombreTipoAccion": juicio.get('nombreTipoAccion')
            }
        
        juicio_cleaned.append(juicio)


    return juicio_cleaned


if __name__ == "__main__":
    info_juicio = get_info_juicio("13284202406765")
    print(info_juicio)