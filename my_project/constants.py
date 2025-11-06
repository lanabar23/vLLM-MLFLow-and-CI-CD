SERVER_URL = '176.108.250.95' # это IP VM в СберКлауудии. Если сервер развернут на локальной машине, то меняем на 'localhost'.

# Порт сервера
SERVER_PORT = 5000

# Полный URL для endpoint predict
PREDICT_URL = f"http://{SERVER_URL}:{SERVER_PORT}/predict"

# Другие возможные константы
# CLIENT_URL = '...'