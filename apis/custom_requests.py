import datetime
import requests
from pysondb import db

proxies = {'http': 'http://v59blt8ofjnzfke-country-ec-session-c4v0ewtp5l-lifetime-1:omxlc0wlg57a0jn@rp.proxyscrape.com:6060'}
max_attempts = 5

def request(method,url,headers,payload):
    for attempt in range(max_attempts):
        try:
            response = requests.request(method, url, headers=headers, data=payload, timeout=3, proxies=proxies)
            if response.status_code in [500,502,503,504]:
                # Retry request 
                continue
            else:
                if attempt > 0:
                    print(f'Ready in attempt: {attempt}')
                break
        except Exception as e:
            print(f'Exteption {e}')
            if attempt == max_attempts-1:
                error_log = {'timestamp':str(datetime.now()),'url': url, "server_response": response.text, "exception": str(e)}
                database = db.getDb('requests_errors.json')
                database.add(error_log)
            pass
    return response