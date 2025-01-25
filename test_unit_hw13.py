import unittest
from hw13_fastapi_app import create_access_token

class TestAccessToken(unittest.TestCase):
    def test_create_access_token(self):
        data = {"sub": "test@example.com"}
        token = create_access_token(data)
        self.assertIsInstance(token, str)
