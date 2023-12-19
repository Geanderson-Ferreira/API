import requests

json_data = {"Status": 'Pendente'}
response = requests.get('http://127.0.0.1:8000/api/list-orders/', json_data)

print(response)