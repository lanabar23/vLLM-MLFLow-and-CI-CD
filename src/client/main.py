import requests

response = requests.get('http://localhost:8080')
print('Привет от сервера: ',response.text)