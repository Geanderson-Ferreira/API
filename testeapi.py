import requests

j = {
    'IdOrder': '1',
    'Status': 1
}

f= requests.get('http://127.0.0.1:8000/api/list-orders/', json=j)

print(f.content)