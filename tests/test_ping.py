import pytest
import subprocess

@pytest.fixture
def server_url():
    return  '5.255.255.77' # "176.108.250.95"  # Замените на ваш IP-адрес

def test_ping_server(server_url):
    try:
        # Выполняем команду ping
        result = subprocess.run(['ping', '-c', '4', server_url], capture_output=True, text=True, check=True)
        # Проверяем, что ping прошел успешно
        assert "4 packets transmitted, 4 received" in result.stdout
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Ошибка при выполнении ping: {e}")