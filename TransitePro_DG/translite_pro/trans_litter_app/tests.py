'''
CSRF‑токен. Для POST‑запросов в Django требуется CSRF‑токен.
Функция getCookie('csrftoken') извлекает его из cookies.
'''


import requests

url = 'http://127.0.0.1:8000/api/'
payload = {'data': 'лиска'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)
print(response.json())

url = 'http://127.0.0.1:8000/history/'

# Тестируем разные значения n
for n in [3, 5,]:
    params = {'n': n}
    response = requests.get(url, params=params)
    print(f"n={n}: {response.json()}")