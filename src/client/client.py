import requests
from constants import PREDICT_URL

def send_request(prompt):
    """
    Метод отправляет запрос на сервер и получает ответ.
    Параметры:
        data (dict): Данные для отправки на сервер.
    Возвращает:
        dict: Полученный ответ от сервера.
    """
    try:
        response = requests.post(PREDICT_URL, json=prompt)
        response.raise_for_status()  # Генерируем исключение, если сервер ответил с ошибкой
        return response.json()
    except Exception as e:
        print(f"Ошибка при отправке запроса: {e}")
        return None

#import requests

#block_for_test client->server
# response = requests.get('http://localhost:8080')
# print('Привет от сервера: ',response.text)

# def send_request(prompt):
#     url = "http://localhost:5000/predict"
#     data = {"text": prompt}
#     response = requests.post(url, json=data)
#     return response.json()["response"]

# if __name__ == "__main__":
#     prompt = input("Введите запрос: ")
#     response = send_request(prompt)
#     print("Ответ:", response)

# EXTERNAL_SERVER_URL = '176.108.250.95'  #внешний IP

# def server_url():
#     return f'http://{EXTERNAL_SERVER_URL}:5000'

# def send_request(prompt):
#     url = server_url() + "/predict"
#     data = {"text": prompt}
#     response = requests.post(url, json=data)
#     return response.json()["response"]

    

# if __name__ == "__main__":
#     prompt = input("Введите запрос: ")
#     response = send_request(prompt)
#     print("Ответ:", response)


