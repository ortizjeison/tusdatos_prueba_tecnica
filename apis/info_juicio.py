import requests
import json


def get_info_juicio(idJuicio):

    proxies = {
   'http': 'http://186.215.87.194:6010',
   'http': 'http://186.103.130.93:8080'
    }

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
    'host': 'api.funcionjudicial.gob.ec',
    'Cookie': 'CJ=2853568778.31775.0000'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=60,proxies=proxies)

    return response.json()


if __name__ == "__main__":
    info_juicio = get_info_juicio("13284202406765")
    print(info_juicio)