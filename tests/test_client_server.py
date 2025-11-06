import pytest
import requests
from ..constants import SERVER_URL

your_server_url = SERVER_URL

@pytest.fixture
def server_url():
    return f'http://{your_server_url}'

def test_get_data(server_url):
    response = requests.get(f"{server_url}/data")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_post_data(server_url):
    payload = {'field': 'value'}
    response = requests.post(f"{server_url}/post-data", json=payload)
    assert response.status_code == 201
    assert response.json()['message'] == 'Success!'