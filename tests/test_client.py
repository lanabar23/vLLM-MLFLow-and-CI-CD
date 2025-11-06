import unittest
import src
from src.client.client import send_request
from .constants import PREDICT_URL

class TestClient(unittest.TestCase):
    def test_send_request(self):
        # Готовим данные для передачи
        request_data = {
            "text": "Привет, как дела?",
        }
        
        # Вызываем клиентскую функцию send_request
        response = send_request(request_data)
        
        # Проверяем правильность ответа
        self.assertIsNotNone(response)
        self.assertIn("response", response)

if __name__ == "__main__":
    unittest.main()


# import unittest
# from src.client.client import send_request

# class TestClient(unittest.TestCase):
#     def test_send_request(self):
#         response = send_request("Привет, как дела?")
#         self.assertIsNotNone(response)

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from src.client.client import send_request

# EXTERNAL_SERVER_URL = '176.108.250.95'  #внешний IP

# class TestClient(unittest.TestCase):
#     def test_send_request(self):
#         response = send_request(f"http://{EXTERNAL_SERVER_URL}/predict", text="Привет, как дела?")
#         self.assertIsNotNone(response)

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from src.client.client import send_request
# from constants import SERVER_URL, SERVER_PORT

# class TestClient(unittest.TestCase):
#     def test_send_request(self):
#         full_url = f"http://{SERVER_URL}:{SERVER_PORT}/predict"
#         response = send_request(full_url, text="Привет, как дела?")
#         self.assertIsNotNone(response)

# if __name__ == "__main__":
#     unittest.main()

