import requests

json_data = {"IdOrder": '1'}
response = requests.get('http://127.0.0.1:8000/api/list-orders/', json_data)

print(response.content)