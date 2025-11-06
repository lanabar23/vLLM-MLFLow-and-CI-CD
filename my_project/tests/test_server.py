import unittest
import requests
from constants import PREDICT_URL


# class TestServer(unittest.TestCase):
#     def test_predict(self):
#         url = f"http://{SERVER_URL}:5000/predict"
#         data = {"text": "Привет, как дела?"}
#         response = requests.post(url, json=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIsNotNone(response.json()["response"])

# if __name__ == "__main__":
#     unittest.main()

class TestServer(unittest.TestCase):
    def test_predict(self):
        data = {"text": "Привет, как дела?"}
        response = requests.post(PREDICT_URL, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json().get("response"))

if __name__ == "__main__":
    unittest.main()

