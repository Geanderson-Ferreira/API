"""

MY_IP = os.getenv('MY_IP')

import requests
import pandas as pd
from src.db_manager.config import MY_IP

def test_list_orders():

    url_complete = f'http://{MY_IP}:8000/api/list-orders/'
    print('>>', url_complete)

    r = requests.get(url_complete)
    print('>> Status Requisicao:',r.status_code)

    if r.status_code == 200:
        j = r.json()
        print('\n', pd.DataFrame(j), '\n')
    else:
        print('>> Result:', r.content)

"""