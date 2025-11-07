#import pytest
import requests
import logging
from constants import SERVER_URL

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

your_server_url = f'http://{SERVER_URL}' #
print(your_server_url)

#@pytest.fixture
# def server_url():
#     return f'http://{SERVER_URL}'  #{your_server_url}'

def test_get_data():
    logging.debug(f"Отправляем GET-запрос на {your_server_url}/data")
    print('get')
    try:
        response = requests.get(f"{your_server_url}/data", timeout=10)
        logging.debug(f"Получен ответ с кодом {response.status_code}")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при отправке GET-запроса: {e}")
        #pytest.fail(f"Ошибка при отправке GET-запроса: {e}")

def test_post_data():
    payload = {'field': 'value'}
    logging.debug(f"Отправляем POST-запрос на {your_server_url}/post-data с данными: {payload}")
    print('post')
    try:
        response = requests.post(f"{your_server_url}/post-data", json=payload, timeout=10)
        logging.debug(f"Получен ответ с кодом {response.status_code}")
        assert response.status_code == 201
        assert response.json()['message'] == 'Success!'
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при отправке POST-запроса: {e}")
        #pytest.fail(f"Ошибка при отправке POST-запроса: {e}")

if __name__=='__main__':
    test_get_data()
    test_post_data()
    
