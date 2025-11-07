#import pytest
import logging
import subprocess
from .constants import SERVER_URL

#@pytest.fixture
def server_url():
    return  '5.255.255.77' # "176.108.250.95"  # Замените на ваш IP-адрес

def test_ping_ip(server_url):
    try:
        # Выполняем команду ping
        result = subprocess.run(['ping', '-c', '4', server_url], capture_output=True, text=True, check=True)
        # Проверяем, что ping прошел успешно
        assert "4 packets transmitted, 4 received" in result.stdout
        logging.debug(f"Ping прошел успешно.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Ошибка Ошибка при выполнении ping: {e}")
        #pytest.fail(f"Ошибка при выполнении ping: {e}")

if __name__=="__name__":
    test_ping_ip(SERVER_URL) #())